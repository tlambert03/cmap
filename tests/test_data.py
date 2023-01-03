from typing import TYPE_CHECKING, cast

import numpy as np
import numpy.testing as npt
import pytest
from cmap import Colormap, data

try:
    import matplotlib as mpl
except ImportError:
    pytest.skip("matplotlib not installed", allow_module_level=True)

MPL_CMAPS = {c for c in mpl.colormaps if not c.endswith("_r")}

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
    if missing := (MPL_CMAPS - set(data._DATA)):
        raise AssertionError(f"missing cmap keys from matplotlib: {missing}")


_gradient = np.linspace(0, 1, 256)


@pytest.mark.parametrize("name", sorted(MPL_CMAPS), ids=str)
def test_matplotlib_image_parity(name) -> None:
    mpl_map = cast("MPLColormap", mpl.colormaps[name])
    our_map = Colormap(getattr(data, name)).to_mpl()
    if isinstance(mpl_map, mpl.colors.ListedColormap):
        pytest.xfail("ListedColormap not supported")
        return
    img1 = mpl_map(_gradient)
    img2 = our_map(_gradient)
    npt.assert_allclose(img1, img2, atol=0.01)


def test_functions() -> None:
    """Testing colormaps from functions"""
    ch = Colormap(data.cubehelix)
    assert ch(0.0) == (0.0, 0.0, 0.0, 1.0)
    npt.assert_allclose(ch(0.5), (0.659019, 0.469366, 0.24845, 1.0), rtol=1e-5)
    assert ch(1.0) == (1.0, 1.0, 1.0, 1.0)
