from __future__ import annotations

from numbers import Number
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    DefaultDict,
    Iterable,
    Iterator,
    NamedTuple,
    Sequence,
    Union,
    cast,
    overload,
)

import numpy as np

from ._color import Color

if TYPE_CHECKING:
    import pygfx
    from bokeh.models import LinearColorMapper as BokehLinearColorMapper
    from matplotlib.colors import LinearSegmentedColormap as MplLinearSegmentedColormap
    from napari.utils.colormaps import Colormap as NapariColormap
    from numpy.typing import ArrayLike, NDArray
    from typing_extensions import Literal, TypeAlias, TypedDict
    from vispy.color import Colormap as VispyColormap

    from ._color import ColorLike, RGBTuple

    class MPLSegmentData(TypedDict):
        red: list[tuple[float, float, float]] | Callable[[np.ndarray], np.ndarray]
        green: list[tuple[float, float, float]] | Callable[[np.ndarray], np.ndarray]
        blue: list[tuple[float, float, float]] | Callable[[np.ndarray], np.ndarray]

    ColorStopLike: TypeAlias = Union[tuple[float, ColorLike], np.ndarray]
    # All of the things that we can pass to the constructor of Colormap
    ColorStopsLike: TypeAlias = Union[
        str,  # single color string or colormap name, w/ optional "_r" suffix
        Iterable[ColorLike | ColorStopLike],
        np.ndarray,
        MPLSegmentData,
        dict[float, ColorLike],
        "ColorStops",
    ]


class Colormap:
    """A colormap is a mapping from scalar values to RGB(A) colors.

    Parameters
    ----------
    color_data : Color | ColorStop | Iterable[Color | ColorStop] | dict[float, Color]
        The color data to use for the colormap. Can be a single color, a single
        color stop, a sequence of colors and/or color stops, or a dictionary
        mapping scalar values to colors.

        Any of the following are valid:

        - a single string color-like value (e.g. "red", "rgb(255, 0, 0)", "#ff0000"),
          in which case the colormap will go from transparent to that color.
        - a recognized string color or colormap name, optionally suffixed with "_r" to
          reverse the colormap (e.g. "viridis", "magma_r").
        - a sequence of color-like values (any object that can be cast to a Color), or
          color-stop-like tuples (a tuple of a scalar value and a color-like value).
          When using color stops, the scalar values should be in the range [0, 1].
          If no scalar stop positions are given, they will be linearly interpolated
          between any neighboring stops (or 0-1 if there are no stops).  See the
          ColorStops class for more details.
        - a dictionary mapping scalar values to color-like values.
        - a matplotlib-style segmentdata dictionary, with keys "red", "green", and
          "blue", each of which maps to a list of tuples of the form (x, y0, y1), or
          a callable that takes an array of values in the range [0, 1] and returns an
          array of RGB(A) values in the range [0, 1].  See the matplotlib docs for more.

    name : str | None
        A name for the colormap. If None, will be set to the identifier or the string
        "custom colormap".
    identifier : str | None
        The identifier of the colormap. If None, will be set to the name, converted
        to lowercase and with spaces and dashes replaced by underscores.
    category : str | None
        An optional category of the colormap (e.g. "diverging", "sequential").  Not
        used internally, but can be useful for applications.
    """

    __slots__ = ("color_stops", "name", "identifier", "category", "_luts")

    color_stops: ColorStops
    name: str
    identifier: str
    category: str | None

    _luts: dict[tuple[int, float], np.ndarray]

    def __init__(
        self,
        color_data: ColorStopsLike,
        *,
        name: str | None = None,
        identifier: str | None = None,
        category: str | None = None,
    ) -> None:
        name = name or identifier or "custom colormap"
        # because we're using __setattr__ to make the object immutable
        object.__setattr__(self, "color_stops", ColorStops.parse(color_data))
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "identifier", _make_identifier(identifier or name))
        object.__setattr__(self, "category", category)
        object.__setattr__(self, "_luts", {})

    def __setattr__(self, _name: str, _value: Any) -> None:
        raise AttributeError("Colormap is immutable")

    def __reduce__(self) -> str | tuple[Any, ...]:
        return self.__class__, (self.color_stops,)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Colormap):
            try:
                other = Colormap(other)  # type: ignore
            except Exception:
                return NotImplemented
        return self.color_stops == other.color_stops

    def lut(self, N: int = 255, gamma: float = 1) -> np.ndarray:
        """Return a lookup table (LUT) for the colormap.

        The returned LUT is a numpy array of RGBA values, with shape (N, 4), where N is
        the number of requested colors in the LUT. The LUT can be used to map scalar
        values (that have been normalized to 0-1) to colors.

        Parameters
        ----------
        N : int
            The number of colors in the LUT.
        gamma : float
            The gamma value to use for the LUT.
        """
        if (N, gamma) not in self._luts:
            self._luts[(N, gamma)] = self.color_stops.to_lut(N, gamma)
        return self._luts[(N, gamma)]

    def __call__(self, X: float | ArrayLike) -> Color | NDArray[np.float64]:
        lut = self.lut()
        xa = np.array(X, copy=True)
        if not xa.dtype.isnative:
            xa = xa.byteswap().newbyteorder()  # Native byteorder is faster.
        if xa.dtype.kind == "f":
            N = len(lut)
            with np.errstate(invalid="ignore"):
                xa *= N
                # Negative values are out of range, but astype(int) would
                # truncate them towards zero.
                xa[xa < 0] = -1
                # xa == 1 (== N after multiplication) is not out of range.
                xa[xa == N] = N - 1
                # Avoid converting large positive values to negative integers.
                np.clip(xa, -1, N, out=xa)
                xa = xa.astype(int)

        result = lut.take(xa, axis=0, mode="clip")
        return result if np.iterable(X) else Color(result)

    def iter_colors(self, N: Iterable[int] | int = 256) -> Iterator[Color]:
        """Return a list of N color objects sampled evenly over the range of the LUT.

        If N is an integer, it will return a list of N colors spanning the full range
        of the colormap. If N is an iterable, it will return a list of colors at the
        positions specified by the iterable.
        """
        nums = np.linspace(0, 1, N) if isinstance(N, int) else np.asarray(N)
        for c in self(nums):
            yield Color(c)

    # -------------------------- RICH REPR SUPPORT ----------------------------------

    def __rich_repr__(self) -> Any:
        from rich import get_console
        from rich.style import Style
        from rich.text import Text

        console = get_console()
        color_cell = Text("")
        X = np.linspace(0, 1.0, console.width - 12, dtype=np.float64)
        for _color in self(X):
            color_cell += Text(" ", style=Style(bgcolor=Color(_color).hex[:7]))
        console.print(color_cell)

    # -------------------------- PYDANTIC SUPPORT -----------------------------------

    @classmethod
    def __get_validators__(cls) -> Iterator[Callable]:
        yield cls._validate  # pydantic validator

    @classmethod
    def _validate(cls, v: Any) -> Colormap:
        return v if isinstance(v, cls) else cls(v)

    # ------------------------- THIRD PARTY SUPPORT ---------------------------------

    def to_mpl(self, N: int = 256, gamma: float = 1.0) -> MplLinearSegmentedColormap:
        """Return a matplotlib colormap."""
        import matplotlib.colors as mplc

        return mplc.LinearSegmentedColormap.from_list(
            self.name, self.color_stops, N=N, gamma=gamma
        )

    def to_vispy(self) -> VispyColormap:
        """Return a vispy colormap."""
        from vispy.color import Colormap

        return Colormap(
            colors=self.color_stops.color_array, controls=self.color_stops.stops
        )

    @overload
    def to_pygfx(
        self, N: int = ..., *, as_view: Literal[True] = ...
    ) -> pygfx.TextureView:
        ...

    @overload
    def to_pygfx(self, N: int = ..., *, as_view: Literal[False]) -> pygfx.Texture:
        ...

    def to_pygfx(
        self, N: int = 256, *, as_view: bool = True
    ) -> pygfx.TextureView | pygfx.Texture:
        """Return a pygfx TextureView, or Texture if as_view is False.

        If you want to customize the TextureView, use `as_view == False` and then
        call `get_view()` on the returned Texture, providing the desired arguments.
        """
        import pygfx

        # TODO: check whether pygfx has it's own stop-aware interpolation,
        # and if so, use that instead of .lut()
        # (get_view has a filter argument... but I don't know whether it will take
        # care of the stops)
        tex = pygfx.Texture(self.lut(N).astype(np.float32), dim=1)
        return tex.get_view() if as_view else tex

    def to_plotly(self) -> list[list[float | str]]:
        """Return a plotly colorscale."""
        # :7 because plotly doesn't support alpha in hex values
        return [[pos, color.rgba_string] for pos, color in self.color_stops]

    def to_napari(self) -> NapariColormap:
        """Return a napari colormap."""
        from napari.utils.colormaps import Colormap

        return Colormap(
            colors=self.color_stops.color_array,
            controls=self.color_stops.stops,
            name=self.identifier or "custom colormap",
            display_name=self.name,
        )

    def to_bokeh(self, N: int = 256) -> BokehLinearColorMapper:
        """Return a bokeh colorscale, with N color samples from the colormap."""
        from bokeh.models import LinearColorMapper

        # TODO: check whether bokeh has it's own interpolation, and if so, use that
        return LinearColorMapper([color.hex for color in self.iter_colors(N)])

    def to_altair(self, N: int = 256) -> list[str]:
        """Return an altair colorscale with N color samples from the colormap.

        Suitable for passing to the range parameter of altair.Scale.
        """
        return [color.hex for color in self.iter_colors(N)]


class ColorStop(NamedTuple):
    """A color stop in a color gradient."""

    position: float
    color: Color


class ColorStops(Sequence[ColorStop]):
    """A sequence of color stops in a color gradient.

    Convenience class allowing various operations on a sequence of color stops,
    including casting to an (N, 5) array (e.g. `np.asarray(ColorStops(...))`)
    """

    _stops: np.ndarray  # internally, stored as an (N, 5) array

    @classmethod
    def parse(  # noqa: C901
        cls,
        colors: ColorStopsLike,
        fill_mode: Literal["neighboring", "fractional"] = "neighboring",
    ) -> ColorStops:
        """Parse `colors` into a sequence of color stops.

        This is the more flexible constructor.t

        Each item in `colors` can be a color, or a 2-tuple of (position, color), where
        position (the "stop" along a color gradient) is a float between 0 and 1.  Where
        not provided, color positions will be evenly distributed between neighboring
        specified positions (if `fill_mode` is 'neighboring') or will be replaced with
        `index / (len(colors)-1)` (if `fill_mode` is 'fractional').

        Colors can be expressed as anything that can be converted to a Color, including
        a string, or 3/4-sequence of RGB(A) values.

        Parameters
        ----------
        colors : str | Iterable[Any]
            Colors and (optional) stop positions.
        fill_mode : {'neighboring', 'fractional'}, optional
            How to fill in missing stop positions.  If 'neighboring' (the default),
            missing positions will be evenly distributed between the closest specified
            neighboring positions.  If 'fractional', missing stop positions will be
            replaced with `index / (len(colors)-1)`.  For example:

            >>> s = ColorStops.parse(['r', 'y', (0.8,'g'), 'b'])
            >>> s.stops
            # 'y' is halfway between 'r' and 'g'
            (0.0, 0.4, 0.8, 1.0)
            >>> s = ColorStops.parse(['r', 'y', (0.8,'g'), 'b'], fill_mode='fractional')
            >>> s.stops
            # 'y' is 1/3 of the way between 0 and 1
            (0.0, 0.3333333333333333, 0.8, 1.0)

        Returns
        -------
        ColorStops
            A sequence of color stops.
        """
        if isinstance(colors, ColorStops):
            return colors

        if fill_mode not in {"neighboring", "fractional"}:
            raise ValueError(
                f"fill_mode must be 'neighboring' or 'fractional', not {fill_mode!r}"
            )

        _clr_seq: Sequence[ColorLike | ColorStopLike]
        if isinstance(colors, str):
            _clr_seq = [colors[:-2], None] if colors.endswith("_r") else [None, colors]
        elif isinstance(colors, dict):
            if all(isinstance(x, Number) for x in colors):
                colors = cast("dict[float, ColorLike]", colors)
                _clr_seq = [(x, colors[x]) for x in sorted(colors)]
            elif {"red", "green", "blue"}.issubset(set(colors)):
                _clr_seq = _mpl_segmentdata_to_stops(cast("MPLSegmentData", colors))
            else:
                raise TypeError(
                    "If colors is a dict, it must be a mapping from position to color, "
                    "or a matplotlib-style segmentdata dict (with 'red', 'green', and "
                    "'blue' keys)."
                )
        else:  # all other iterables
            _clr_seq = list(colors)

        if len(_clr_seq) == 1:
            _clr_seq = [None, _clr_seq[0]]

        _positions: list[float | None] = []
        _colors: list[Color] = []
        for item in _clr_seq:
            if isinstance(item, (tuple, list)) and len(item) == 2:
                # a 2-tuple cannot be a valid color, so it must be a stop
                _position, item = cast("tuple[float, ColorLike]", item)
            elif (isinstance(item, (tuple, list)) and len(item) == 5) or (
                isinstance(item, np.ndarray) and item.shape == (5,)
            ):
                # 5-element vector must be (position, r, g, b, a)
                _position, *item = cast("Sequence[float]", item)
            else:
                _position = None
            _positions.append(_position)
            _colors.append(Color(item))  # this will raise if invalid

        _stops = _fill_stops(_positions, fill_mode)

        return ColorStops(zip(_stops, _colors))

    def __init__(self, stops: np.ndarray | Iterable[tuple[float, Color]]) -> None:
        # the internal representation is an (N, 5) array
        # the first column is the stop position, the next 4 are the RGBA values
        if isinstance(stops, np.ndarray):
            if stops.shape[1] != 5:
                raise ValueError("Expected (N, 5) array")
            self._stops = stops
        else:
            self._stops = np.array([(p,) + tuple(c) for p, c in stops])

    @property
    def stops(self) -> tuple[float, ...]:
        """Return tuple of color stop positions."""
        return tuple(self._stops[:, 0])

    @property
    def colors(self) -> tuple[Color, ...]:
        """Return all colors as Color objects."""
        return tuple(Color(c) for c in self.color_array)

    @property
    def color_array(self) -> np.ndarray:
        """Return an (N, 4) array of RGBA values."""
        return self._stops[:, 1:]

    def __len__(self) -> int:
        return len(self._stops)

    @overload
    def __getitem__(self, key: int) -> ColorStop:
        ...

    @overload
    def __getitem__(self, key: slice) -> ColorStops:
        ...

    @overload
    def __getitem__(self, key: tuple) -> np.ndarray:
        ...

    def __getitem__(
        self, key: int | slice | tuple
    ) -> ColorStop | ColorStops | np.ndarray:
        """Get an item or slice of the color stops.

        If key is an integer, return a single `ColorStop` tuple.
        If key is a slice, return a new `ColorStops` object.
        If key is a tuple, return a numpy array (standard numpy indexing).
        """
        # sourcery skip: assign-if-exp, reintroduce-else
        if isinstance(key, slice):
            return ColorStops(self._stops[key])
        if isinstance(key, tuple):
            return np.asarray(self)[key]  # type: ignore
        pos, *rgba = self._stops[key]
        return ColorStop(pos, Color(rgba))

    def __array__(self) -> np.ndarray:
        """Return (N, 5) array, N rows of (position, r, g, b, a)."""
        return self._stops

    def __repr__(self) -> str:
        m = ",\n  ".join(repr((pos, Color(rgba))) for pos, *rgba in self._stops)
        return f"ColorStops(\n  {m}\n)"

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, ColorStops):
            try:
                __o = ColorStops.parse(__o)  # type: ignore
            except Exception:
                return NotImplemented
        return np.array_equal(self._stops, __o._stops)

    @classmethod
    def __get_validators__(cls) -> Iterator[Callable]:
        yield cls.parse  # pydantic validator

    def to_lut(self, N: int = 256, gamma: float = 1.0) -> np.ndarray:
        """Create (N, 4) LUT of RGBA values, interpolated between color stops."""
        return _interpolate_stops(N, self, gamma)

    def __reversed__(self) -> Iterator[ColorStop]:
        for pos, *rgba in self._stops[::-1]:
            # reverse the colors, but not the positions
            yield ColorStop(1 - pos, Color(rgba))


def _fill_stops(
    stops: Iterable[float | None], fill_mode: Literal["neighboring", "fractional"]
) -> list[float]:
    """Fill in missing stop positions.

    Replace None values in the list of stop positions with values spaced evenly
    between the nearest non-`None` values.

    Parameters
    ----------
    stops : list[float | None]
        List of stop positions.
    fill_mode : {'neighboring', 'fractional'}
        If 'neighboring', fill in missing stops with evenly spaced values between
        the nearest non-`None` values. If 'fractional', fill in missing stops with
        evenly spaced values between 0 and 1.

    Examples
    --------
    >>> fill_stops([0.0, None, 0.5, None, 1.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    >>> fill_stops([None, None, None])
    [0.0, 0.5, 1.0]
    >>> fill_stops([None, None, 0.8, None, 1.0])
    [0.0, 0.4, 0.8, 0.9, 1.0]
    """
    _stops = list(stops)
    if not _stops:
        return []

    if fill_mode == "fractional":
        N = len(_stops) - 1
        return [i / N if s is None else s for i, s in enumerate(_stops)]

    # make edges 0-1 unless they are explicitly set
    if _stops[0] is None:
        _stops[0] = 0.0
    if _stops[-1] is None:
        _stops[-1] = 1.0

    out: list[float] = []
    last_val: tuple[int, float] = (0, 0.0)
    in_gap = False  # marks whether we are in a series of Nones
    for idx, stop in enumerate(_stops):
        if stop is not None:
            if in_gap:
                # if we are at the first value after a series of Nones, then
                # fill in the Nones with values spaced evenly between the
                # previous value and the current value.
                _idx, _stop = last_val
                filler = np.linspace(_stop, stop, idx - _idx + 1)
                out.extend(filler[1:])
                in_gap = False
            else:
                # otherwise, just append the current value
                out.append(stop)
            last_val = (idx, stop)
        else:
            in_gap = True
    return out


def _interpolate_stops(N: int, data: ArrayLike, gamma: float = 1.0) -> np.ndarray:
    """Intperpolate (R, C) array of values to an (N, C-1) LUT array.

    The input array must have at least 2 columns, where the first column is a
    monotonically increasing list of positions from 0 to 1, and the remaining columns
    are vector values to interpolate between (such as r, g, b, a values). For example:

        [[0.0, 0.0, 0.0, 0.0, 0.0],  # transparent black
         [0.5, 1.0, 0.0, 0.0, 1.0],  # opaque red
         [1.0, 1.0, 1.0, 1.0, 1.0]]  # opaque white

    (Note, this function does not assume 5 columns, and will work with any
    number of columns greater than 1.)

    The output array will have N rows, and C-1 columns (i.e. the first column will
    no longer represent positions, and each row will be an interpolated value of the
    remaining columns of the input array). For a color LUT, each row represents
    the color at an evenly spaced position along the color gradient, from 0 to 1.

    This array can be used to create a color map, or to apply a color gradient to data
    that has been normalized to the range 0-1. (e.g. lut.take(data * (N-1), axis=0))

    Parameters
    ----------
    N : int
        Number of interpolated values to generate in the output LUT.
    data : ArrayLike
        Array of (position, r, g, b, a) values.
    gamma : float, optional
        Gamma correction to apply to the output LUT, by default 1.0

    Returns
    -------
    lut : np.ndarray
        (N, 4) LUT of RGBA values, interpolated between color stops.
    """
    adata = np.atleast_2d(np.array(data))
    if adata.shape[1] < 2:
        raise ValueError("data must have at least 2 columns")

    # make sure the first and last stops are at 0 and 1 ...
    # adding additional control points that copy the first/last color if needed
    if adata[0, 0] != 0.0:
        adata = np.vstack([[0.0, *adata[0, 1:]], adata])
    if adata[-1, 0] != 1.0:
        adata = np.vstack([adata, [1.0, *adata[-1, 1:]]])

    x = adata[:, 0]
    rgba = adata[:, 1:]

    if (np.diff(x) < 0).any():
        raise ValueError("Color stops must be in ascending position order")

    # begin generation of lookup table
    if N == 1:
        # convention: use the y = f(x=1) value for a 1-element lookup table
        lut = rgba[-1]
    else:
        # sourcery skip: extract-method
        # scale stop positions to the number of elements (-1) in the LUT
        x = x * (N - 1)
        # create evenly spaced LUT indices with gamma correction
        xind = np.linspace(0, 1, N) ** gamma
        # scale to the number of elements (-1) in the LUT, and exclude exterior values
        xind = ((N - 1) * xind)[1:-1]
        # Find the indices in the scaled positions array `x` that each element in
        # `xind` would need to be inserted before to maintain order.
        ind = np.searchsorted(x, xind)
        # calculate the fractional distance between the two values in `x` that
        # each element in `xind` is between. (this is the position at which we need
        # to sample between the neighboring color stops)
        frac_dist = (xind - x[ind - 1]) / (x[ind] - x[ind - 1])
        # calculate the color at each position in `xind` by linearly interpolating
        # the value at `frac_dist` between the neighboring color stops
        start = rgba[ind - 1]
        length = rgba[ind] - start
        interpolated_points = frac_dist[:, np.newaxis] * length + start
        # concatenate the first and last color stops with the interpolated values
        lut = np.concatenate([[rgba[0]], interpolated_points, [rgba[-1]]])

    # ensure that the lut is confined to values between 0 and 1 by clipping it
    return np.clip(lut, 0.0, 1.0)  # type: ignore


def _mpl_segmentdata_to_stops(
    data: MPLSegmentData, precision: int = 16, N: int = 256, gamma: float = 1.0
) -> list[tuple[float, RGBTuple]]:
    """Converts a matplotlib colormap segmentdata dict to a list of stops.

    Parameters
    ----------
    data : dict
        A matplotlib colormap segmentdata dict, with keys 'red', 'green', 'blue' and
        values that are either a sequence of (X, Y0, Y1) tuples, or a callable
        function that takes an array of indices and returns an array of values.
    precision : int, optional
        The number of decimal places to round the output values to, by default 16
    N : int, optional
        The number of values to generate for the output stops (only used if any value
        in the data dict is a callable), by default 256
    gamma : float, optional
        The gamma correction to apply to the output stops, by default 1.0 (only used
        if any value in the data dict is a callable)

    Returns
    -------
    stops : list[tuple[float, RGBTuple]]
        A list of (position, [r, g, b]) tuples.
    """
    out: DefaultDict[float, list[float]] = DefaultDict(lambda: [0, 0, 0])
    for index, color in enumerate(("red", "green", "blue")):
        cdata = data[color]  # type: ignore
        if callable(cdata):
            xind = np.linspace(0, 1, N) ** gamma
            values = np.clip(np.array(cdata(xind), dtype=float), 0, 1)
            for x, y in zip(xind, values):
                out[x][index] = round(y, precision)
        else:
            for x, y, _ in cdata:
                out[x][index] = round(y, precision)
    return [(k, tuple(out[k])) for k in sorted(out)]  # type: ignore


def _make_identifier(name: str) -> str:
    """Return a valid Python identifier from a string."""
    out = "".join(c for c in name if c.isalnum() or c in ("_", "-", " "))
    return out.lower().replace(" ", "_").replace("-", "_")
