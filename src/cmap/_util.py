from typing import Sequence

import numpy as np

from cmap import Colormap, data

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))


def plot_color_gradients(cmap_list: Sequence[str], use_mpl: bool = False) -> None:
    # Create figure and adjust figure height to number of colormaps
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    nrows = len(cmap_list)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows + 1, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh, left=0.2, right=0.99)

    for ax, name in zip(axs, cmap_list):
        cm = mpl.colormaps[name] if use_mpl else Colormap(getattr(data, name)).to_mpl()
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

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()
