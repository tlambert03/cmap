from __future__ import annotations
from functools import partial

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
    TypedDict,
    Union,
    cast,
    overload,
)

import numpy as np
import numpy.typing as npt

from . import _external
from ._color import Color

if TYPE_CHECKING:
    import pygfx
    from bokeh.models import LinearColorMapper as BokehLinearColorMapper
    from matplotlib.colors import LinearSegmentedColormap as MplLinearSegmentedColormap
    from matplotlib.figure import Figure as MplFigure
    from napari.utils.colormaps import Colormap as NapariColormap
    from numpy.typing import ArrayLike, NDArray
    from typing_extensions import Literal, TypeAlias, TypeGuard
    from vispy.color import Colormap as VispyColormap

    from ._color import ColorLike

    LutCallable: TypeAlias = Callable[[NDArray], NDArray]
    ColorStopLike: TypeAlias = Union[tuple[float, ColorLike], np.ndarray]
    # All of the things that we can pass to the constructor of Colormap
    ColorStopsLike: TypeAlias = Union[
        str,  # single color string or colormap name, w/ optional "_r" suffix
        Iterable[ColorLike | ColorStopLike],
        np.ndarray,
        "MPLSegmentData",
        dict[float, ColorLike],
        "ColorStops",
        LutCallable,
    ]


class MPLSegmentData(TypedDict):
    red: list[tuple[float, float, float]] | Callable[[np.ndarray], np.ndarray]
    green: list[tuple[float, float, float]] | Callable[[np.ndarray], np.ndarray]
    blue: list[tuple[float, float, float]] | Callable[[np.ndarray], np.ndarray]


class ColormapDict(TypedDict):
    name: str
    identifier: str
    category: str | None
    color_stops: list[tuple[float, list[float]]]


class Colormap:
    """A colormap is a mapping from scalar values to RGB(A) colors.

    Parameters
    ----------
    color_stops : Color | ColorStop | Iterable[Color | ColorStop] | dict[float, Color]
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
          ColorStops class for more details. (Note that a ColorStops instance
          may also be used here)
        - a dictionary mapping scalar values to color-like values: e.g.
          {0.0: "red", 0.5: (0, 1, 0), 1.0: "#0000FF"}.
        - a matplotlib-style segmentdata dictionary, with keys "red", "green", and
          "blue", each of which maps to a list of tuples of the form (x, y0, y1), or
          a callable that takes an array of values in the range [0, 1] and returns an
          array of values in the range [0, 1].  See the matplotlib docs for more.
        - a callable that takes an array of N values in the range [0, 1] and returns an
          (N, 4) array of RGBA values in the range [0, 1].

    name : str | None
        A name for the colormap. If None, will be set to the identifier or the string
        "custom colormap".
    identifier : str | None
        The identifier of the colormap. If None, will be set to the name, converted
        to lowercase and with spaces and dashes replaced by underscores.
    category : str | None
        An optional category of the colormap (e.g. "diverging", "sequential").
        Not used internally.
    source : str | None
        An optional source or reference for the colormap (e.g. "matplotlib", "napari").
        Not used internally.
    """

    __slots__ = (
        "color_stops",
        "name",
        "identifier",
        "category",
        "source",
        "_luts",
        "__weakref__",
    )

    color_stops: ColorStops
    name: str
    identifier: str
    category: str | None
    source: str | None

    _luts: dict[tuple[int, float], np.ndarray]

    def _json_encode(self) -> ColormapDict:
        return self.as_dict()

    def __init__(
        self,
        color_stops: ColorStopsLike,
        *,
        name: str | None = None,
        identifier: str | None = None,
        category: str | None = None,
        source: str | None = None,
    ) -> None:
        name = name or identifier or "custom colormap"
        # because we're using __setattr__ to make the object immutable
        object.__setattr__(self, "color_stops", ColorStops.parse(color_stops))
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "identifier", _make_identifier(identifier or name))
        object.__setattr__(self, "category", category)
        object.__setattr__(self, "source", source)
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

    def as_dict(self) -> ColormapDict:
        """Return a dictionary representation of the colormap.

        The returned dictionary is suitable for serialization, or for passing to the
        Colormap constructor.
        """
        return {
            "name": self.name,
            "identifier": self.identifier,
            "category": self.category,
            "color_stops": [(p, list(c)) for p, c in self.color_stops],
        }

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

    def __call__(
        self, X: float | ArrayLike, *, N: int = 255, gamma: float = 1
    ) -> Color | NDArray[np.float64]:
        lut = self.lut(N=N, gamma=gamma)
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

    def __repr__(self) -> str:
        # in case we're in init
        name = getattr(self, "name", None)
        n_stops = len(self.color_stops) if hasattr(self, "color_stops") else 0
        return f"Colormap(name={name!r}, {n_stops} colors)"

    # -------------------------- RICH REPR SUPPORT ----------------------------------

    def __rich_repr__(self) -> Any:
        return _external.rich_print_colormap(self)  # side effect

    # -------------------------- PYDANTIC SUPPORT -----------------------------------

    @classmethod
    def __get_validators__(cls) -> Iterator[Callable]:
        yield cls._validate  # pydantic validator

    @classmethod
    def _validate(cls, v: Any) -> Colormap:
        if isinstance(v, cls):
            return v  # pragma: no cover
        return cls(**v) if isinstance(v, dict) else cls(v)

    # ------------------------- THIRD PARTY SUPPORT ---------------------------------

    def to_mpl(self, N: int = 256, gamma: float = 1.0) -> MplLinearSegmentedColormap:
        """Return a matplotlib colormap."""
        return _external.to_mpl(self, N=N, gamma=gamma)

    def to_vispy(self) -> VispyColormap:
        """Return a vispy colormap."""
        return _external.to_vispy(self)

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
        return _external.to_pygfx(self, N=N, as_view=as_view)

    def to_napari(self) -> NapariColormap:
        """Return a napari colormap.

        https://napari.org/stable/api/napari.utils.Colormap.html
        """
        return _external.to_napari(self)

    def to_plotly(self) -> list[list[float | str]]:
        """Return a plotly colorscale."""
        return _external.to_plotly(self)

    def to_bokeh(self, N: int = 256) -> BokehLinearColorMapper:
        """Return a bokeh colorscale, with N color samples from the colormap.

        https://docs.bokeh.org/en/latest/docs/reference/models/mappers.html

        Parameters
        ----------
        N : int, optional
            Number of colors to sample from the colormap, by default 256.
        """
        return _external.to_bokeh(self, N=N)

    def to_altair(self, N: int = 256) -> list[str]:
        """Return an altair colorscale with N color samples from the colormap.

        Suitable for passing to the range parameter of altair.Scale.
        https://altair-viz.github.io/user_guide/customization.html#color-domain-and-range
        """
        return _external.to_altair(self, N=N)

    def visualize(self, dpi: int = 100, dest: str | None = None) -> MplFigure:
        """Plot colormap using viscm.  (Requires viscm to be installed.).

        https://github.com/matplotlib/viscm

        Parameters
        ----------
        dpi : int, optional
            dpi for saved image. Defaults to 100.
        dest : str, optional
            If provided, the image will be saved to this path. Defaults to None.
        """
        return _external.viscm_plot(self, dpi, dest)


class ColorStop(NamedTuple):
    """A color stop in a color gradient."""

    position: float
    color: Color


class ColorStops(Sequence[ColorStop]):
    """A sequence of color stops in a color gradient.

    Convenience class allowing various operations on a sequence of color stops,
    including casting to an (N, 5) array (e.g. `np.asarray(ColorStops(...))`)

    This is the main internal representation of a colormap, and is used to construct
    the LUT used in the Colormap.__call__ method.
    """

    _stops: np.ndarray  # internally, stored as an (N, 5) array

    @classmethod
    def parse(  # noqa: C901
        cls,
        colors: ColorStopsLike,
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

        Returns
        -------
        ColorStops
            A sequence of color stops.
        """
        if isinstance(colors, ColorStops):
            return colors
        if callable(colors):
            return cls.from_callable(colors)

        _clr_seq: Sequence[ColorLike | ColorStopLike]
        if isinstance(colors, str):
            _clr_seq = [colors[:-2], None] if colors.endswith("_r") else [None, colors]
        elif isinstance(colors, dict):
            if _is_mpl_segmentdata(colors):
                _mpl_stops = _mpl_segmentdata_to_stops(colors)
                if callable(_mpl_stops):
                    return cls.from_callable(_mpl_stops)
                _clr_seq = _mpl_stops
            elif all(isinstance(x, Number) for x in colors):
                colors = cast("dict[float, ColorLike]", colors)
                _clr_seq = [(x, colors[x]) for x in sorted(colors)]
            else:
                raise ValueError(
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

        if (np.diff([x for x in _positions if x is not None]) < 0).any():
            raise ValueError("Color stops must be in ascending position order")

        _stops = _fill_stops(_positions, "neighboring")  # TODO: expose fill_mode?

        return ColorStops(zip(_stops, _colors))

    @classmethod
    def from_color_array(cls, colors: ArrayLike) -> ColorStops:
        """Create ColorStops from an (N, 3) or (N, 4) array-like.

        This is a faster constructor for creating a ColorStops from a numeric
        array-like of 3- or 4-element color vectors.  e.g.

        - [[0, 0, 0], [1, 1, 1]]
        - [[0, 0, 0, 1], [1, 1, 1, 1]]
        - [Color('green'), Color('red')]

        Returns
        -------
        ColorStops
            A sequence of color stops.
        """
        _colors = np.atleast_2d(np.asarray(colors))
        if np.issubdtype(_colors.dtype, int) and _colors.max() > 1:
            # assume 8 bit colors
            _colors = np.clip(_colors.astype(float) / 255, 0, 1)
        elif not np.issubdtype(_colors.dtype, np.number):
            raise ValueError("Expected numeric array")  # pragma: no cover
        if _colors.shape[1] == 3:
            # add alpha channel
            _colors = np.concatenate([_colors, np.ones((_colors.shape[0], 1))], axis=1)
        elif _colors.shape[1] != 4:  # pragma: no cover
            raise ValueError("Expected (N, 3) or (N, 4) array")
        # add stop positions
        stops = np.linspace(0, 1, _colors.shape[0])
        _colors = np.concatenate([stops[:, None], _colors], axis=1)
        return cls(_colors)

    @classmethod
    def from_callable(
        cls,
        func: Callable[[NDArray[np.floating]], NDArray],
        N: int | Sequence[float] = 256,
    ) -> ColorStops:
        """Create ColorStops from a callable that returns an (N, 4) array.

        We sample this function at N evenly spaced positions between 0 and 1, and
        use the resulting colors as the color stops.

        Examples
        --------
        >>> ColorStops.from_callable(lambda x: np.array([[1, 0, 0, 1]]))
        ColorStops([(0.0, Color('red')), (1.0, Color('red'))])
        """
        stops = np.linspace(0, 1, N) if isinstance(N, int) else np.array(N)
        colors = np.clip(func(stops), 0, 1)
        if len(colors) != len(stops):
            raise ValueError(  # pragma: no cover
                f"Requested {len(stops)} colors, but function returned {len(colors)}"
            )
        return cls.from_color_array(colors)

    def __init__(self, stops: np.ndarray | Iterable[tuple[float, Color]]) -> None:
        # the internal representation is an (N, 5) array
        # the first column is the stop position, the next 4 are the RGBA values
        if isinstance(stops, np.ndarray):
            if len(stops.shape) != 2 or stops.shape[1] != 5:
                raise ValueError("Expected (N, 5) array")  # pragma: no cover
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

    def __array__(self, dtype: npt.DTypeLike = None) -> np.ndarray:
        """Return (N, 5) array, N rows of (position, r, g, b, a)."""
        return self._stops if dtype is None else self._stops.astype(dtype)

    def __repr__(self) -> str:
        m = ",\n  ".join(repr((pos, Color(rgba))) for pos, *rgba in self._stops)
        return f"ColorStops(\n  {m}\n)"

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, ColorStops):
            try:
                __o = ColorStops.parse(__o)  # type: ignore
            except Exception:
                return NotImplemented
        return np.allclose(self._stops, __o._stops)

    def to_lut(self, N: int = 255, gamma: float = 1.0) -> np.ndarray:
        """Create (N, 4) LUT of RGBA values, interpolated between color stops.

        Parameters
        ----------
        N : int
            Number of colors to return.
        gamma : float
            Gamma correction to apply to the colors.
        """
        if 100 < len(self._stops) == N + 1:
            # no interpolation needed
            return self.color_array
        return _interpolate_stops(N, self._stops, gamma)

    def __reversed__(self) -> Iterator[ColorStop]:
        for pos, *rgba in self._stops[::-1]:
            # reverse the colors, but not the positions
            yield ColorStop(1 - pos, Color(rgba))

    @classmethod
    def __get_validators__(cls) -> Iterator[Callable]:
        yield cls.parse  # pydantic validator

    def _json_encode(self) -> list:
        return cast(list, self._stops.tolist())


def _fill_stops(
    stops: Iterable[float | None],
    fill_mode: Literal["neighboring", "fractional"] = "neighboring",
) -> list[float]:
    """Fill in missing stop positions.

    Replace None values in the list of stop positions with values spaced evenly
    between the nearest non-`None` values.

    Parameters
    ----------
    stops : list[float | None]
        List of stop positions.
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

    Examples
    --------
    >>> fill_stops([0.0, None, 0.5, None, 1.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    >>> fill_stops([None, None, None])
    [0.0, 0.5, 1.0]
    >>> fill_stops([None, None, 0.8, None, 1.0])
    [0.0, 0.4, 0.8, 0.9, 1.0]
    """
    if fill_mode not in {"neighboring", "fractional"}:
        raise ValueError(  # pragma: no cover
            f"fill_mode must be 'neighboring' or 'fractional', not {fill_mode!r}"
        )

    _stops = list(stops)
    if not _stops:
        return []  # pragma: no cover

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
    if adata.shape[1] < 2:  # pragma: no cover
        raise ValueError("data must have at least 2 columns")

    # make sure the first and last stops are at 0 and 1 ...
    # adding additional control points that copy the first/last color if needed
    if adata[0, 0] != 0.0:
        adata = np.vstack([[0.0, *adata[0, 1:]], adata])
    if adata[-1, 0] != 1.0:
        adata = np.vstack([adata, [1.0, *adata[-1, 1:]]])

    x = adata[:, 0]
    rgba = adata[:, 1:]

    # This is also validated in the ColorMap constructor...
    # so we can skip it here unless this becomes a public function
    # if (np.diff(x) < 0).any():  # pragma: no cover
    #     raise ValueError("Color stops must be in ascending position order")

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


def _map_rgb(mappers: Iterable[LutCallable], ary: "NDArray") -> "NDArray":
    """Helper function for combining multiple LutCallables into single rgb array."""
    return np.stack([_g(np.asarray(ary)) for _g in mappers], axis=-1)


def _mpl_segmentdata_to_stops(
    data: MPLSegmentData, precision: int = 16, N: int = 256, gamma: float = 1.0
) -> list[ColorStopLike] | LutCallable:
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
    if all(callable(v) for v in data.values()):
        return partial(_map_rgb, (data["red"], data["green"], data["blue"]))
    if any(callable(v) for v in data.values()):
        raise ValueError(
            "All values in segmentdata dict must be either callable or a sequence"
        )
    rgb_stops = [
        [i[:2] for i in data[c]] for c in ("red", "green", "blue")  # type: ignore
    ]
    all_positions = np.array(sorted({i for n in rgb_stops for i, _ in n}))
    rgb = [np.interp(all_positions, *np.asarray(s).T) for s in rgb_stops]
    rgba = np.stack(rgb + [np.ones_like(all_positions)], axis=1)
    return [(a, tuple(b)) for a, b in zip(all_positions, rgba.tolist())]


def _make_identifier(name: str) -> str:
    """Return a valid Python identifier from a string."""
    out = "".join(c for c in name if c.isalnum() or c in ("_", "-", " "))
    return out.lower().replace(" ", "_").replace("-", "_")


def _is_mpl_segmentdata(obj: Any) -> TypeGuard[MPLSegmentData]:
    """Return True if obj is a matplotlib segmentdata dict."""
    return isinstance(obj, dict) and all(k in obj for k in ("red", "green", "blue"))
