import numpy as np
import pytest
from cmap._color import RGBA, RGBA8, Color


@pytest.mark.parametrize(
    "color, expected",
    [
        ("royalblue", (65, 105, 225)),
        (Color("royalblue"), (65, 105, 225)),
        ("Royal Blue", (65, 105, 225)),
        ((65, 105, 225), (65, 105, 225)),
        ([65, 105, 225], (65, 105, 225)),
        (np.array([65, 105, 225]), (65, 105, 225)),
        (RGBA8(65, 105, 225), (65, 105, 225)),
        ("rgb(65, 105, 225)", (65, 105, 225)),
        ("rgb(65 105 225)", (65, 105, 225)),
        ("rgb(65,105,225)", (65, 105, 225)),
        ((65 / 255, 105 / 255, 225 / 255), (65, 105, 225)),
        ("#4169E1", (65, 105, 225)),
        ("#ABC", (170, 187, 204)),
        (0x4169E1, (65, 105, 225)),
        ("0x4169E133", (65, 105, 225, 0.2)),
        ("rgb(2, 3, 4)", (2, 3, 4)),
        ("rgb(100%, 0%, 0%)", (255, 0, 0)),
        ("rgb(100%,none, 0%)", (255, 0, 0)),
        ("rgba(2, 3, 4, 0.5)", (2, 3, 4, 0.5)),
        ("rgba(2,3,4,50%)", (2, 3, 4, 0.5)),
        ("rgb(-2, 3, 4)", (0, 3, 4)),
        ("rgb(100, 200, 300)", (100, 200, 255)),
        ("rgb(20, 10, 0, -10)", (20, 10, 0, 0)),
        ("rgb(100%, 200%, 300%)", (255, 255, 255)),
        ("rgb(100%, 200%, 300%)", (255, 255, 255)),
        ("rgb(128 none none / none)", (128, 0, 0, 0)),
        ("hsl(120, 100%, 50%)", (0, 255, 0)),
        ("hsla(120, 100%, 50%, 0.25)", (0, 255, 0, 0.25)),
        ("hsla(120, 100%, 50% / none)", (0, 255, 0, 0)),
        (RGBA(0, 1, 0, 0), (0, 255, 0, 0)),
        (RGBA8(0, 255, 0, 1), (0, 255, 0, 1)),
        (None, (0, 0, 0, 0)),
    ],
)
def test_rgb_parse(color: str, expected: tuple) -> None:
    assert RGBA8.parse(color)[: len(expected)] == expected
    assert RGBA.parse(color).to_8bit()[: len(expected)] == expected


def test_color_errors() -> None:
    with pytest.raises(ValueError, match="Invalid color string"):
        Color("rgb(100%, 200%, 300%, 400%, 500%)")
    with pytest.raises(ValueError, match="Invalid color string"):
        Color("seven")
    with pytest.raises(TypeError, match="Cannot convert typ"):
        Color(1.2)
    with pytest.raises(AttributeError, match="Color is immutable"):
        Color("red")._rgba = 1


def test_conversions() -> None:
    # this test is very sensitive to rounding errors
    start = RGBA8(59, 84, 226, 0.6)
    assert start == start.to_float().to_8bit()
    assert start == start.to_hsl().to_rgba().to_8bit()
    assert start == start.to_hsv().to_rgba().to_8bit()
    assert int(start.to_hsl().in_degrees()[0]) == 231
    assert start.to_hex() == start.to_float().to_hex() == "#3B54E299"
    assert str(start) == str(start.to_float()) == "#3B54E299"
