import sys
from typing import Sequence

import numpy as np

from cmap import Colormap, data

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))


def plot_color_gradients(cmap_list: Sequence[str], compare: bool = False) -> None:
    # Create figure and adjust figure height to number of colormaps
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    nrows = len(cmap_list) * (2 if compare else 1)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows + 1, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh, left=0.2, right=0.99)

    for i, (ax, name) in enumerate(zip(axs[::2 if compare else 1], cmap_list)):
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
                'mpl',
                va="center",
                ha="right",
                fontsize=10,
                transform=ax2.transAxes,
            )

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    plot_color_gradients(sys.argv[1:], compare=True)
    plt.show()
