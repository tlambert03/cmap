import sys
from typing import TYPE_CHECKING, Sequence

import numpy as np

from cmap import Colormap, data

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

if TYPE_CHECKING:
    from matplotlib.figure import Figure as MplFigure


def plot_color_gradients(cmap_list: Sequence[str], compare: bool = False) -> None:
    # Create figure and adjust figure height to number of colormaps
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    nrows = len(cmap_list) * (2 if compare else 1)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows + 1, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh, left=0.2, right=0.99)

    for i, (ax, name) in enumerate(zip(axs[:: 2 if compare else 1], cmap_list)):
        cm = Colormap(getattr(data, name)).to_mpl()
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
        if compare:
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


def plot_rgb(cmap: Colormap, N: int = 256) -> "MplFigure":
    """Plot the R,G,B,A components of a colormap individually."""
    import matplotlib.pyplot as plt

    x = np.linspace(0, 1, N)
    fig, ax = plt.subplots()
    colors = cmap(x, N=N)
    ax.plot(x, colors[:, 0], color="r", label="Red")
    ax.plot(x, colors[:, 1], color="g", label="Green")
    ax.plot(x, colors[:, 2], color="b", label="Blue")
    ax.plot(x, colors[:, 3], color="k", label="Alpha", linestyle="--", alpha=0.5)
    return fig


def plot_lightness(cmap: Colormap, N: int = 100, reverse: bool = False) -> None:
    """Plot L* component of a colormap in CAM02-UCS color space over range 0-1."""
    import matplotlib.pyplot as plt

    try:
        from colorspacious import cspace_converter
    except ImportError as e:
        raise ImportError(
            "This function requires the colorspacious package. "
            "Please `pip install colorspacious` and try again."
        ) from e

    x = np.linspace(0.0, 1.0, N)
    rgb = cmap(x)[None, :, :3]
    lab = cspace_converter("sRGB1", "CAM02-UCS")(rgb)
    lslice = np.s_[::-1] if reverse else np.s_[:]
    y_ = lab[0, lslice, 0]
    c_ = x[lslice]

    if hasattr(cmap, "to_mpl"):
        cmap = cmap.to_mpl()
    plt.scatter(x, y_, c=c_, cmap=cmap, s=250, linewidths=0)
    plt.plot(x, y_, c="black", linewidth=1, alpha=0.2)
    plt.gca().set_ylabel("Lightness $L^*$", fontsize=12)
    plt.gca().set_xlabel("Value", fontsize=12)
    plt.show()


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    plot_color_gradients(sys.argv[1:], compare=True)
    plt.show()
