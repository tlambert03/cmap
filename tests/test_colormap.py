import numpy.testing as npt
import pytest
from cmap import Color, Colormap


def test_colormap() -> None:
    """Test Colormap."""
    cmap = Colormap(["red", "magenta", "blue"])
    assert cmap(0.0) == (1, 0, 0, 1)
    assert cmap(0.0) is Color("r")
    assert cmap(0.5) == (1, 0, 1, 1)
    assert cmap(0.5) is Color("m")
    assert cmap(1.0) == (0, 0, 1, 1)
    assert cmap(1.0) is Color("b")
    assert cmap(1.5) == (0, 0, 1, 1)

    npt.assert_array_equal(
        cmap([0, 0.5, 1.0]), [(1, 0, 0, 1), (1, 0, 1, 1), (0, 0, 1, 1)]
    )


def test_colormap_copy() -> None:
    """Test Colormap copy."""
    import pickle
    from copy import copy, deepcopy

    cmap1 = Colormap(["red", "magenta", "blue"])
    cmap2 = Colormap(["r", (0.5, "magenta"), "b"])
    assert cmap1 == cmap2
    assert copy(cmap1) == cmap1
    assert deepcopy(cmap1) == cmap1
    assert cmap1 == ["r", "m", "b"]
    assert cmap1 == ["r", (0.5, "m"), "b"]
    assert cmap1 == pickle.loads(pickle.dumps(cmap1)) == cmap2
    assert cmap1 != {"1234"}


def test_colormap_errors() -> None:
    with pytest.raises(AttributeError, match="Colormap is immutable"):
        Colormap("red")._luts = {}


def test_colormap_methods() -> None:
    cmap1 = Colormap(["red", "magenta", "blue"])
    assert cmap1 == [(0, "r"), (0.5, "m"), (1, "b")]
    assert list(cmap1.color_stops) == [(0, "r"), (0.5, "m"), (1, "b")]
    assert Colormap(reversed(cmap1.color_stops)) == Colormap(["b", "m", "r"])
    assert list(cmap1.iter_colors(3)) == [Color("r"), Color("m"), Color("b")]
