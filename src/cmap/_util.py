from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Sequence, cast

import numpy as np

from cmap import Colormap

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

if TYPE_CHECKING:
    from matplotlib.figure import Figure as MplFigure
    from numpy.typing import ArrayLike


def _ensure_cmap(cmap: Colormap | str) -> Colormap:
    cm = Colormap(cmap) if isinstance(cmap, str) else cmap
    if not isinstance(cm, Colormap):
        raise TypeError(f"Expected Colormap or str, got {type(cm)}")
    return cm


def plot_color_gradients(
    cmap_list: Sequence[str | Colormap], compare: bool = False
) -> MplFigure:
    # Create figure and adjust figure height to number of colormaps
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    nrows = len(cmap_list) * (2 if compare else 1)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows + 1, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh, left=0.2, right=0.99)

    for i, (ax, name) in enumerate(zip(axs[:: 2 if compare else 1], cmap_list)):
        cm = _ensure_cmap(name).to_mpl()
        ax.imshow(gradient, aspect="auto", cmap=cm)
        ax.text(
            -0.01,
            0.5,
            name,
            va="center",
            ha="right",
            fontsize=10,
            transform=ax.transAxes,
        )
        if compare and name in mpl.colormaps:
            cm2 = mpl.colormaps[name]
            ax2 = axs[i * 2 + 1]
            ax2.imshow(gradient, aspect="auto", cmap=cm2)
            ax2.text(
                -0.01,
                0.5,
                "mpl",
                va="center",
                ha="right",
                fontsize=10,
                transform=ax2.transAxes,
            )

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()
    return fig

def plot_rgb(cmap: Colormap | str, N: int = 256) -> "MplFigure":
    """Plot the R,G,B,A components of a colormap individually."""
    import matplotlib.pyplot as plt

    x = np.linspace(0, 1, N)
    fig, ax = plt.subplots()
    colors = _ensure_cmap(cmap)(x, N=N)
    ax.plot(x, colors[:, 0], color="r", label="Red")
    ax.plot(x, colors[:, 1], color="g", label="Green")
    ax.plot(x, colors[:, 2], color="b", label="Blue")
    ax.plot(x, colors[:, 3], color="k", label="Alpha", linestyle="--", alpha=0.5)
    return fig


def calc_lightness(
    cmap: Colormap | str, x: ArrayLike | None = None, colorspace: str = "CAM02-UCS"
) -> np.ndarray:
    """Calculate the L* component of a colormap in CAM02-UCS over range 0-1.

    Parameters
    ----------
    cmap : Colormap
        The colormap to calculate lightness for.
    x : np.ndarray, optional
        The values to calculate lightness for, by default np.linspace(0.0, 1.0, 101)
    colorspace : str, optional
        The colorspace to calculate lightness in, by default "CAM02-UCS"
    """
    try:
        from colorspacious import cspace_converter
    except ImportError as e:
        raise ImportError(
            "This function requires the colorspacious package. "
            "Please `pip install colorspacious` and try again."
        ) from e

    x = np.linspace(0.0, 1.0, 101) if x is None else np.asarray(x)
    rgb = _ensure_cmap(cmap)(x)[None, :, :3]
    lab = cspace_converter("sRGB1", colorspace)(rgb)
    return cast("np.ndarray", lab[0, :, 0])


def plot_lightness(
    cmap: Colormap | str,
    x: ArrayLike | None = None,
    colorspace: str = "CAM02-UCS",
    reverse: bool = False,
) -> MplFigure:
    """Plot L* component of a colormap in `colorspace` over range 0-1.

    see colorspacious docs for valid colorspace strings:
    https://colorspacious.readthedocs.io/en/latest/reference.html#supported-colorspaces

    Parameters
    ----------
    cmap : Colormap
        The colormap to calculate lightness for.
    x : np.ndarray, optional
        The values to calculate lightness for, by default np.linspace(0.0, 1.0, 101)
    colorspace : str, optional
        The colorspace to calculate lightness in, by default "CAM02-UCS"
    reverse : bool, optional
        Whether to reverse the colormap, by default False
    """
    import matplotlib.pyplot as plt

    x = np.linspace(0.0, 1.0, 101) if x is None else np.asarray(x)
    cmap = _ensure_cmap(cmap)
    lab = calc_lightness(cmap, x, colorspace)
    lslice = np.s_[::-1] if reverse else np.s_[:]
    y_ = lab[lslice]
    c_ = x[lslice]

    if hasattr(cmap, "to_mpl"):
        cmap = cmap.to_mpl()

    fig, ax = plt.subplots()
    ax.scatter(x, y_, c=c_, cmap=cmap, s=250, linewidths=0)
    ax.plot(x, y_, c="black", linewidth=1, alpha=0.2)
    ax.set_ylabel("Lightness $L^*$", fontsize=12)
    ax.set_xlabel("Value", fontsize=12)
    ax.set_ylim(-5, 105)
    ax.grid(True, alpha=0.2)
    return fig


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    plot_color_gradients(sys.argv[1:], compare=True)
    plot_lightness(sys.argv[1])
    plt.show()
