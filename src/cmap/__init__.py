"""Scientific colormaps for python, without dependencies."""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("cmap")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "uninstalled"

from ._color import HSLA, HSVA, RGBA, RGBA8, Color
from ._colormap import Colormap, ColorStop, ColorStops

__all__ = [
    "Color",
    "Colormap",
    "ColorStop",
    "ColorStops",
    "HSLA",
    "HSVA",
    "RGBA",
    "RGBA8",
]
