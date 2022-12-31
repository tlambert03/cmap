from unittest.mock import MagicMock, patch

import pytest
from cmap import Color


def test_pydantic_support() -> None:
    pydantic = pytest.importorskip("pydantic.color")

    assert Color(pydantic.Color("red")) is Color("red")


def test_colour_support() -> None:
    colour = pytest.importorskip("colour")
    assert Color(colour.Color("red")) is Color("red")


def test_rich_repr() -> None:
    rich = pytest.importorskip("rich")
    from rich.text import Text

    mock = MagicMock()
    with patch.object(rich, "get_console", lambda: mock):
        Color("red").__rich_repr__()
    mock.print.assert_called_once_with(Text("  ", style="on red"), end="")
