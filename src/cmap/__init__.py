"""Scientific colormaps for python, without dependencies."""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("cmap")
except PackageNotFoundError:
    __version__ = "uninstalled"

from ._color import HSLA, HSVA, RGBA, RGBA8, Color
from ._colormap import Colormap, ColorStops

__all__ = [
    "Color",
    "Colormap",
    "ColorStops",
    "HSLA",
    "HSVA",
    "RGBA",
    "RGBA8",
]
