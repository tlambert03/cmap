# Overview

`cmap` is a work-in-progress colormap library for python, providing all of the colormaps
in matplotlib, napari, vispy (and more), with no dependencies beyond numpy.

Many libraries that use colormaps end up either depending on matplotlib, vendoring the
colormaps, or reimplementing them. This library aims to provide a single source of truth
for colormaps, and to provide a simple API for using them in a variety of other libraries (currently including, matplotlib, napari, vispy, pygfx, bokeh, plotly, altair, and more).

More docs to follow.

See the [Colormaps catalog](catalog/index.md) for a list of all available colormaps.
