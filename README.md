# cmap

[![License](https://img.shields.io/pypi/l/cmap.svg?color=green)](https://github.com/tlambert03/cmap/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/cmap.svg?color=green)](https://pypi.org/project/cmap)
[![Python Version](https://img.shields.io/pypi/pyversions/cmap.svg?color=green)](https://python.org)
[![CI](https://github.com/tlambert03/cmap/actions/workflows/ci.yml/badge.svg)](https://github.com/tlambert03/cmap/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/tlambert03/cmap/branch/main/graph/badge.svg)](https://codecov.io/gh/tlambert03/cmap)

Scientific colormaps for python, with no dependencies beyond numpy.

With `cmap`, you can use any of the colormaps from [matplotlib](https://matplotlib.org/stable/tutorials/colors/colormaps.html) or [cmocean](https://matplotlib.org/cmocean/) in your python code, without having to install matplotlib or cmocean.

There are a number of python libraries that provide or require colormaps or
basic color support, but they all either depend on matplotlib, provide a
specialized set of colormaps intended to extend those provided by matplotlib, or
roll their own colormap solution that vendors/duplicates other libraries.

`cmap` is a lightweight, library that provides all of the open-source colormaps
from matplotlib and cmocean, with no dependencies beyond numpy.  It provides
exports to a number of known third-party colormap objects, allowing it to be
used across a wide range of python visualization libraries.  The intention is to provide
a library that can be used by any python library that needs colormaps, without
forcing the user to install matplotlib (while still being compatible with matplotlib
and other libraries that use matplotlib colormaps).

`cmap` is strictly typed and fully tested, with a focus on good developer experience.

## API

### `cmap.Color`

The `cmap.Color` object is a simple wrapper around a tuple of RGBA scalars, with
a few convenience methods for converting to other color objects.  It can parse a
variety of inputs, including:

- a string name of a color (e.g. `"red"`, `"green"`, `"blue"`) or any of the CSS level 4 color names
- an RGB or RGBA hex string (e.g. `"#ff0000"`, `"#0000ff99"`)
- a string `rgba` or `hsla` [CSS specifier](https://w3c.github.io/csswg-drafts/css-color/#rgb-functions)
  (e.g. `"rgba(255, 0, 0, 1)"`, `"hsla(0, 100%, 50%, 0.5)"`)
- a 3- or 4-tuple of floats from 0-1 (e.g. `(1, 0.5, 0)`, `(0, 0, 1, 0.6)`)
- a 3- or 4-tuple of ints from 0-255 with optional float alpha (e.g. `(255, 128,
  0)`, `(0, 0, 255, 0.5)`) (*note that alpha is **always** a float between 0 and
  1*)
- a numpy array of shape `(3,)` or `(4,)`, interpreted as above for 3- or 4-tuples
- a `cmap.Color` object
- a [`pydantic.color.Color` object](https://docs.pydantic.dev/usage/types/#color-type)
- a [`colour.Color` object](https://github.com/vaab/colour)

```python
from cmap import Color

red = Color("red")
```

### `cmap.Colormap`

The `cmap.Colormap` object is a callable that can map a scalar value (or numpy
array of values) to an RGBA color (or a numpy array of RGBA colors).  It can be
initialized with a variety of inputs, including:

- a single color-like string, in which case the colormap goes from transparent to `color`.
- a sequence of color-like objects (see things that can be parsed to colors above)
- a sequence 2-tuples of `(floats, color-like)`, where the floats are
  interpreted as the positions of the colors along the colormap.  If the floats
  are not provided, they are assumed to be evenly spaced.  (note that single color-likes
  and color-stop-like tuples can be combined in the same sequence).
- a `cmap.Colormap` object
- an `(N, 5)` numpy array of N colors, where each row is `(position, r, g, b, a)`
  (`position` must be a monotically increasing float between 0-1).

```python
In [1]: import cmap

In [2]: cmap1 = cmap.Colormap(["red", "green", "blue"])

In [3]: cmap1(np.linspace(0,1,5))
Out[3]:
array([[1.        , 0.        , 0.        , 1.        ],
       [0.50393701, 0.24900417, 0.        , 1.        ],
       [0.        , 0.50196078, 0.        , 1.        ],
       [0.        , 0.24900417, 0.50393701, 1.        ],
       [0.        , 0.        , 1.        , 1.        ]])
```

#### `cmap.ColorStops`

Each `Colormap` has a `color_stops` attribute that is an instance of `cmap.ColorStops`.

This represents the parsed colors and their positions along the colormap.  It can
be cast to an (N, 5) numpy array (position, r, g, b, a), and provides a number of object-oriented api conveniences (`.colors`, `.stops`, `__getitem__`, `to_lut`).

## Current Third Party Support

The `cmap.Colormap` object has convenience methods that allow it to be used with a number of third-party colormap objects.  If you would like to see support added for a particular library, please open an issue or PR.

- [matplotlib](https://matplotlib.org/stable/tutorials/colors/colormaps.html):
  `cmap.Colormap.to_mpl()`
- [vispy](https://vispy.org/): `cmap.Colormap.to_vispy()`
- [napari](https://napari.org/): `cmap.Colormap.to_napari()`
- [pygfx](https://pygfx.readthedocs.io/): `cmap.Colormap.to_pygfx()`
- [plotly](https://plotly.com/python/): `cmap.Colormap.to_plotly()`
- [bokeh](https://docs.bokeh.org/): `cmap.Colormap.to_bokeh()`
- [altair](https://altair-viz.github.io/): `cmap.Colormap.to_altair()`
<!-- - [pyqtgraph](http://www.pyqtgraph.org/)
    - `cmap.Colormap.to_pyqtgraph()` -->

... details to come ...

## Alternatives

Other libraries providing colormaps:

> TODO: list other colormap libraries, their dependencies, and their primary features.

- [matplotlib](https://matplotlib.org/stable/tutorials/colors/colormaps.html)
- [seaborn](https://seaborn.pydata.org/tutorial/color_palettes.html)  (subclasses matplotlib)
- [proplot](https://proplot.readthedocs.io/en/latest/colormaps.html)  (subclasses matplotlib)
- [palettable](https://jiffyclub.github.io/palettable/) (mostly data, import doesn't depend on matplotlib, but usage largely does)
- [cmocean](https://matplotlib.org/cmocean/) (mostly data, outputs matplotlib colormaps)
- [colorcet](https://colorcet.holoviz.org/) (mostly data, usage requires either matplotlib or bokeh)
- [cmasher](https://cmasher.readthedocs.io/) (requires matplotlib)
- [cmyt](https://github.com/yt-project/cmyt) (requires matplotlib)
- [cmcrameri](https://github.com/callumrollo/cmcrameri) (requires matplotlib, wraps <https://www.fabiocrameri.ch/colourmaps/>)
- [distinctipy](https://github.com/alan-turing-institute/distinctipy)  (generates distinct color sets, only requires numpy)
- [Farrow & Ball Matplotlib](https://github.com/vork/farrowandball) (requires matplotlib)
- [mplcyberpunk](https://github.com/dhaitz/mplcyberpunk) (requires matplotlib)

## References and Further reading

- [Choosing Colormaps in Matplotlib](https://matplotlib.org/stable/tutorials/colors/colormaps.html)
- [A Better Default Colormap for Matplotlib | SciPy 2015 | Nathaniel Smith and Stéfan van der Walt](https://www.youtube.com/watch?v=xAoljeRJ3lU)
- blog post for above video: <https://bids.github.io/colormap/>
- [Origins of Colormaps, Cleve Moler, February 2, 2015](https://blogs.mathworks.com/cleve/2015/02/02/origins-of-colormaps/)
- [Documenting the matplotlib colormaps, @endolith](https://gist.github.com/endolith/2719900)
- [Color Map Advice for Scientific Visualization](https://www.kennethmoreland.com/color-advice/)
- <https://colorcet.com/>, Peter Kovesi
- [Kovesi: Good Colour Maps: How to Design Them.](https://arxiv.org/abs/1509.03700)
- https://www.fabiocrameri.ch/colourmaps/
