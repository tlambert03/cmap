from typing import TYPE_CHECKING, Set, cast

import numpy as np
import numpy.testing as npt
import pytest
from cmap import Colormap, data

try:
    import matplotlib as mpl

    MPL_CMAPS: Set[str] = {c for c in mpl.colormaps if not c.endswith("_r")}
except ImportError:
    MPL_CMAPS = {}

_GRADIENT = np.linspace(0, 1, 256)

if TYPE_CHECKING:
    from matplotlib.colors import Colormap as MPLColormap


def test_lower_map() -> None:
    # make sure the lower map is the same length as the original
    # ... i.e. that we have no name collisions
    assert len(data._DATA_LOWER) == len(data._DATA)


def test_data_loading() -> None:
    assert data.__dir__() == list(data._DATA)

    for name in data._DATA:
        Colormap(getattr(data, name))


def test_matplotlib_name_parity() -> None:
    if not MPL_CMAPS:
        pytest.skip("matplotlib not installed")
    if missing := (MPL_CMAPS - set(data._DATA)):
        raise AssertionError(f"missing cmap keys from matplotlib: {missing}")


def test_napari_name_parity() -> None:
    # might need to importorskip later
    import napari.utils.colormaps.colormap_utils as ncm
    from vispy.color import colormap

    napari_cmaps = set(ncm.AVAILABLE_COLORMAPS)
    napari_cmaps.update(ncm._VISPY_COLORMAPS_ORIGINAL)
    napari_cmaps.update(ncm._MATPLOTLIB_COLORMAP_NAMES)
    # TODO: later it would be good to make sure we can accept all strings
    # without having to do any extra work
    napari_cmaps = {
        n.lower().replace(" ", "_")
        for n in napari_cmaps
        if not n.endswith(("_r", " r"))
    }
    our_cmaps = {n.lower() for n in data._DATA}
    if missing := (napari_cmaps - our_cmaps):
        raise AssertionError(f"missing cmap keys from napari: {missing}")


@pytest.mark.parametrize("name", sorted(MPL_CMAPS), ids=str)
def test_matplotlib_image_parity(name: str) -> None:
    mpl_map = cast("MPLColormap", mpl.colormaps[name])
    our_map = Colormap(getattr(data, name))
    our_map_to_mpl = our_map.to_mpl()
    if isinstance(mpl_map, mpl.colors.ListedColormap):
        pytest.xfail("ListedColormap not supported")
        return
    img1 = mpl_map(_GRADIENT)
    img2 = our_map_to_mpl(_GRADIENT)
    img3 = our_map(_GRADIENT)
    atol = 0.25 if name == "gist_stern" else 0.02  # TODO

    npt.assert_allclose(img1, img2, atol=atol)
    npt.assert_allclose(img1, img3, atol=atol)


def test_cubehelix() -> None:
    """Testing colormaps from functions, using cubehelix as an example."""
    ch = Colormap(data.cubehelix)
    assert ch(0.0) == (0.0, 0.0, 0.0, 1.0)
    npt.assert_allclose(ch(0.5), (0.632842, 0.474798, 0.290702, 1.0), rtol=1e-5)
    assert ch(1.0) == (1.0, 1.0, 1.0, 1.0)


def test_mpl_conversion() -> None:
    from cmap._colormap import _mpl_segmentdata_to_stops

    data = {
        "red": (
            (0.00, 0, 0),
            (0.35, 0, 0),
            (0.66, 1, 1),
            (0.89, 1, 1),
            (1.00, 0.5, 0.5),
        ),
        "green": (
            (0.000, 0, 0),
            (0.125, 0, 0),
            (0.375, 1, 1),
            (0.640, 1, 1),
            (0.910, 0, 0),
            (1.000, 0, 0),
        ),
        "blue": (
            (0.00, 0.5, 0.5),
            (0.11, 1, 1),
            (0.34, 1, 1),
            (0.65, 0, 0),
            (1.00, 0, 0),
        ),
    }

    expected = [
        (0.0, (0.0, 0.0, 0.5, 1.0)),
        (0.11, (0.0, 0.0, 1.0, 1.0)),
        (0.125, (0.0, 0.0, 1.0, 1.0)),
        (0.34, (0.0, 0.86, 1.0, 1.0)),
        (0.35, (0.0, 0.9, 0.9677419354838711, 1.0)),
        (0.375, (0.08064516129032263, 1.0, 0.8870967741935485, 1.0)),
        (0.64, (0.9354838709677419, 1.0, 0.032258064516129004, 1.0)),
        (0.65, (0.9677419354838709, 0.9629629629629629, 0.0, 1.0)),
        (0.66, (1.0, 0.9259259259259258, 0.0, 1.0)),
        (0.89, (1.0, 0.07407407407407418, 0.0, 1.0)),
        (0.91, (0.909090909090909, 0.0, 0.0, 1.0)),
        (1.0, (0.5, 0.0, 0.0, 1.0)),
    ]

    result = _mpl_segmentdata_to_stops(data)
    for (rstop, rcolor), (estop, ecolor) in zip(result, expected):
        assert rstop == estop
        assert np.allclose(rcolor, ecolor)
