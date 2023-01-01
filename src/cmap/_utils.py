"""Utility functions and sample images for testing colormaps."""
from __future__ import annotations

import contextlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from matplotlib.colors import Colormap as MPLColormap
    from matplotlib.pyplot import Figure as MPLFigure

    from ._colormap import Colormap


def viscm_plot(
    cmap: Colormap | MPLColormap, dpi: int = 100, dest: str | None = None
) -> MPLFigure:
    """Evaluate goodness of colormap using perceptual deltas.

    Parameters
    ----------
    cmap : Colormap
        Colormap instance.
    dpi : int, optional
        dpi for saved image. Defaults to 100.
    dest : str, optional
        If provided, the image will be saved to this path. Defaults to None.

    """
    try:
        # XXX: this is to avoid an import provlem in viscm, until the fix is released
        # https://github.com/matplotlib/viscm/issues/61
        import matplotlib.backends.backend_qt4agg  # noqa: F401
    except ImportError:
        import sys
        from unittest.mock import MagicMock

        sys.modules["matplotlib.backends.backend_qt4agg"] = MagicMock()

    try:
        import matplotlib.pyplot as plt
        from viscm import viscm
    except ModuleNotFoundError as e:  # pragma: no cover
        raise type(e)(
            "viscm and matplotlib is required to use this method. "
            "Please `pip install viscm`."
        ) from e

    if hasattr(cmap, "to_mpl"):
        cmap = cmap.to_mpl()

    viscm(cmap)
    fig = plt.gcf()
    fig.set_size_inches(16, 8)
    with contextlib.suppress(AttributeError):
        fig.canvas.manager.set_window_title(cmap.name)

    if dest:
        fig.savefig(dest, bbox_inches="tight", dpi=dpi)
    else:
        plt.show()  # pragma: no cover
    return fig
