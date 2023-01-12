"""Colormap catalog.

notes combined from
Peter Kovesi's: https://colorcet.com
mpl docs: https://matplotlib.org/stable/tutorials/colors/colormaps.html#qualitative
colorbrewer2.org: https://colorbrewer2.org

## sequential

- from maptplotlib docs:
    sequential change in lightness and often saturation of color incrementally, often
    using a single hue; should be used for representing information that has ordering.

- from colorcet.com:
    Lightness values increase or decrease monotonically/linearly

- from colorbrewer2.org
    sequential schemes are suited to ordered data that progress from low to high.
    Lightness steps dominate the look of these schemes, with light colors for low data
    values to dark colors for high data values.


## diverging

- from maptplotlib docs:
    diverging: change in lightness and possibly saturation of two different colors that
    meet in the middle at an unsaturated color; should be used when the information
    being plotted has a critical middle value, such as topography or when the data
    deviates around zero.

- from colorcet.com:
    Center point will be black, gray or white. Suitable where the data being displayed
    has a well defined reference value and we are interested in differentiating values
    that lie above, or below the reference value.  In general, diverging colour maps
    have a small perceptual flat spot at the centre. The exception being
    linear-diverging maps which avoid this problem.

- from colorbrewer2.org:
    diverging schemes put equal emphasis on mid-range critical values and extremes at
    both ends of the data range. The critical class or break in the middle of the legend
    is emphasized with light colors and low and high extremes are emphasized with dark
    colors that have contrasting hues.

## cyclic
- from maptplotlib docs:
    change in lightness of two different colors that meet in the middle and
    beginning/end at an unsaturated color; should be used for values that wrap around at
    the endpoints, such as phase angle, wind direction, or time of day.

- from colorcet.com:
    Have colours that are matched at each end. They are intended for the
    presentation of data that is cyclic such as orientation values or angular phase
    data. They require particular care in their design (the standard colour circle is
    not a good map).


## qualitative
- from maptplotlib docs:
    Often are miscellaneous colors; should be used to represent information
    which does not have ordering or relationships.

- from colorbrewer2.org
    qualitative schemes do not imply magnitude differences between legend classes,
    and hues are used to create the primary visual differences between classes.
    qualitative schemes are best suited to representing nominal or categorical data.


## miscellaneous

from matplotlib, catch all for "other" colormaps


colorcet further defines:
Rainbow: It is suggested that they be avoided because they have reversals in the
lightness gradient at yellow and red which can upset a viewer's perceptual ordering of
the colours in the colour map. However, they are attractive and perhaps can have a
legitimate use where the main aim is to differentiate data values rather than
communicate a data ordering.


Isoluminant: Constructed from colours of equal perceptual lightness.
These colour maps are designed for use with relief shading. On their own these colour
maps are not very useful because features in the data are very hard to discern. However,
when used in conjunction with relief shading their constant lightness means that the
colour map does not induce an independent shading pattern that will interfere with, or
even hide, the structures induced by the relief shading. The relief shading provides the
structural information and the colours provide the data classification information.


"Perceptual Uniformity":
is the concept that perceived distances between colors are proportional to
the distances of the values they represent.
- https://onlinelibrary.wiley.com/doi/full/10.1111/cgf.14313

(i.e. there are no "kinks" in the lightness plot as a function of the data.)
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Iterator, Literal, Mapping, cast

if TYPE_CHECKING:
    from typing_extensions import NotRequired, TypeAlias, TypedDict

    from ._colormap import ColorStopsLike

    Category: TypeAlias = Literal[
        "sequential", "diverging", "cyclic", "qualitative", "miscellaneous"
    ]

    class CatalogItem(TypedDict):
        data: str
        category: Category
        tags: NotRequired[list[str]]
        interpolation: NotRequired[bool]
        info: NotRequired[str]

    # would be nice to subclass CatalogItem... but can't
    # https://github.com/python/mypy/issues/7435
    class LoadedCatalogItem(TypedDict):
        data: ColorStopsLike
        tags: list[str]
        category: Category
        interpolation: NotRequired[bool]
        license: str
        source: str
        info: str

    CatalogDict: TypeAlias = dict[str, CatalogItem]

CATALOG: CatalogDict = {
    "Accent": {
        "data": "cmap.data._colorbrewer:Accent_8",
        "category": "qualitative",
        "interpolation": False,
    },
    "Accent_3": {
        "data": "cmap.data._colorbrewer:Accent_3",
        "category": "qualitative",
        "interpolation": False,
    },
    "Accent_4": {
        "data": "cmap.data._colorbrewer:Accent_4",
        "category": "qualitative",
        "interpolation": False,
    },
    "Accent_5": {
        "data": "cmap.data._colorbrewer:Accent_5",
        "category": "qualitative",
        "interpolation": False,
    },
    "Accent_6": {
        "data": "cmap.data._colorbrewer:Accent_6",
        "category": "qualitative",
        "interpolation": False,
    },
    "Accent_7": {
        "data": "cmap.data._colorbrewer:Accent_7",
        "category": "qualitative",
        "interpolation": False,
    },
    "Accent_8": {
        "data": "cmap.data._colorbrewer:Accent_8",
        "category": "qualitative",
        "interpolation": False,
    },
    "BOP_Blue": {
        "data": "cmap.data._leterrier:BOP_Blue",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "BOP_Orange": {
        "data": "cmap.data._leterrier:BOP_Orange",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "BOP_Purple": {
        "data": "cmap.data._leterrier:BOP_Purple",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "Blues": {
        "data": "cmap.data._colorbrewer:Blues_9",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "Blues_3": {
        "data": "cmap.data._colorbrewer:Blues_3",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Blues_4": {
        "data": "cmap.data._colorbrewer:Blues_4",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Blues_5": {
        "data": "cmap.data._colorbrewer:Blues_5",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Blues_6": {
        "data": "cmap.data._colorbrewer:Blues_6",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Blues_7": {
        "data": "cmap.data._colorbrewer:Blues_7",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Blues_8": {
        "data": "cmap.data._colorbrewer:Blues_8",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Blues_9": {
        "data": "cmap.data._colorbrewer:Blues_9",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "BrBG": {
        "data": "cmap.data._colorbrewer:BrBG_11",
        "category": "diverging",
    },
    "BrBG_10": {
        "data": "cmap.data._colorbrewer:BrBG_10",
        "category": "diverging",
        "interpolation": False,
    },
    "BrBG_11": {
        "data": "cmap.data._colorbrewer:BrBG_11",
        "category": "diverging",
        "interpolation": False,
    },
    "BrBG_3": {
        "data": "cmap.data._colorbrewer:BrBG_3",
        "category": "diverging",
        "interpolation": False,
    },
    "BrBG_4": {
        "data": "cmap.data._colorbrewer:BrBG_4",
        "category": "diverging",
        "interpolation": False,
    },
    "BrBG_5": {
        "data": "cmap.data._colorbrewer:BrBG_5",
        "category": "diverging",
        "interpolation": False,
    },
    "BrBG_6": {
        "data": "cmap.data._colorbrewer:BrBG_6",
        "category": "diverging",
        "interpolation": False,
    },
    "BrBG_7": {
        "data": "cmap.data._colorbrewer:BrBG_7",
        "category": "diverging",
        "interpolation": False,
    },
    "BrBG_8": {
        "data": "cmap.data._colorbrewer:BrBG_8",
        "category": "diverging",
        "interpolation": False,
    },
    "BrBG_9": {
        "data": "cmap.data._colorbrewer:BrBG_9",
        "category": "diverging",
        "interpolation": False,
    },
    "BuGn": {
        "data": "cmap.data._colorbrewer:BuGn_9",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "BuGn_3": {
        "data": "cmap.data._colorbrewer:BuGn_3",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "BuGn_4": {
        "data": "cmap.data._colorbrewer:BuGn_4",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "BuGn_5": {
        "data": "cmap.data._colorbrewer:BuGn_5",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "BuGn_6": {
        "data": "cmap.data._colorbrewer:BuGn_6",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "BuGn_7": {
        "data": "cmap.data._colorbrewer:BuGn_7",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "BuGn_8": {
        "data": "cmap.data._colorbrewer:BuGn_8",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "BuGn_9": {
        "data": "cmap.data._colorbrewer:BuGn_9",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "BuPu": {
        "data": "cmap.data._colorbrewer:BuPu_9",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "BuPu_3": {
        "data": "cmap.data._colorbrewer:BuPu_3",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "BuPu_4": {
        "data": "cmap.data._colorbrewer:BuPu_4",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "BuPu_5": {
        "data": "cmap.data._colorbrewer:BuPu_5",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "BuPu_6": {
        "data": "cmap.data._colorbrewer:BuPu_6",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "BuPu_7": {
        "data": "cmap.data._colorbrewer:BuPu_7",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "BuPu_8": {
        "data": "cmap.data._colorbrewer:BuPu_8",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "BuPu_9": {
        "data": "cmap.data._colorbrewer:BuPu_9",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "CMRmap": {
        "data": "cmap.data._CMRmap:CMRmap",
        "category": "miscellaneous",
    },
    "Dark2": {
        "data": "cmap.data._colorbrewer:Dark2_8",
        "category": "qualitative",
        "interpolation": False,
    },
    "Dark2_3": {
        "data": "cmap.data._colorbrewer:Dark2_3",
        "category": "qualitative",
        "interpolation": False,
    },
    "Dark2_4": {
        "data": "cmap.data._colorbrewer:Dark2_4",
        "category": "qualitative",
        "interpolation": False,
    },
    "Dark2_5": {
        "data": "cmap.data._colorbrewer:Dark2_5",
        "category": "qualitative",
        "interpolation": False,
    },
    "Dark2_6": {
        "data": "cmap.data._colorbrewer:Dark2_6",
        "category": "qualitative",
        "interpolation": False,
    },
    "Dark2_7": {
        "data": "cmap.data._colorbrewer:Dark2_7",
        "category": "qualitative",
        "interpolation": False,
    },
    "Dark2_8": {
        "data": "cmap.data._colorbrewer:Dark2_8",
        "category": "qualitative",
        "interpolation": False,
    },
    "GnBu": {
        "data": "cmap.data._colorbrewer:GnBu_9",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "GnBu_3": {
        "data": "cmap.data._colorbrewer:GnBu_3",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "GnBu_4": {
        "data": "cmap.data._colorbrewer:GnBu_4",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "GnBu_5": {
        "data": "cmap.data._colorbrewer:GnBu_5",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "GnBu_6": {
        "data": "cmap.data._colorbrewer:GnBu_6",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "GnBu_7": {
        "data": "cmap.data._colorbrewer:GnBu_7",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "GnBu_8": {
        "data": "cmap.data._colorbrewer:GnBu_8",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "GnBu_9": {
        "data": "cmap.data._colorbrewer:GnBu_9",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Greens": {
        "data": "cmap.data._colorbrewer:Greens_9",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "Greens_3": {
        "data": "cmap.data._colorbrewer:Greens_3",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Greens_4": {
        "data": "cmap.data._colorbrewer:Greens_4",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Greens_5": {
        "data": "cmap.data._colorbrewer:Greens_5",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Greens_6": {
        "data": "cmap.data._colorbrewer:Greens_6",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Greens_7": {
        "data": "cmap.data._colorbrewer:Greens_7",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Greens_8": {
        "data": "cmap.data._colorbrewer:Greens_8",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Greens_9": {
        "data": "cmap.data._colorbrewer:Greens_9",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Greys": {
        "data": "cmap.data._colorbrewer:Greys_9",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "Greys_3": {
        "data": "cmap.data._colorbrewer:Greys_3",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Greys_4": {
        "data": "cmap.data._colorbrewer:Greys_4",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Greys_5": {
        "data": "cmap.data._colorbrewer:Greys_5",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Greys_6": {
        "data": "cmap.data._colorbrewer:Greys_6",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Greys_7": {
        "data": "cmap.data._colorbrewer:Greys_7",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Greys_8": {
        "data": "cmap.data._colorbrewer:Greys_8",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Greys_9": {
        "data": "cmap.data._colorbrewer:Greys_9",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "I_Blue": {
        "data": "cmap.data._leterrier:I_Blue",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "I_Bordeaux": {
        "data": "cmap.data._leterrier:I_Bordeaux",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "I_Cyan": {
        "data": "cmap.data._leterrier:I_Cyan",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "I_Forest": {
        "data": "cmap.data._leterrier:I_Forest",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "I_Green": {
        "data": "cmap.data._leterrier:I_Green",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "I_Magenta": {
        "data": "cmap.data._leterrier:I_Magenta",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "I_Orange": {
        "data": "cmap.data._leterrier:I_Orange",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "I_Purple": {
        "data": "cmap.data._leterrier:I_Purple",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "I_Red": {
        "data": "cmap.data._leterrier:I_Red",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "I_Yellow": {
        "data": "cmap.data._leterrier:I_Yellow",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "OrRd": {
        "data": "cmap.data._colorbrewer:OrRd_9",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "OrRd_3": {
        "data": "cmap.data._colorbrewer:OrRd_3",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "OrRd_4": {
        "data": "cmap.data._colorbrewer:OrRd_4",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "OrRd_5": {
        "data": "cmap.data._colorbrewer:OrRd_5",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "OrRd_6": {
        "data": "cmap.data._colorbrewer:OrRd_6",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "OrRd_7": {
        "data": "cmap.data._colorbrewer:OrRd_7",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "OrRd_8": {
        "data": "cmap.data._colorbrewer:OrRd_8",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "OrRd_9": {
        "data": "cmap.data._colorbrewer:OrRd_9",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Oranges": {
        "data": "cmap.data._colorbrewer:Oranges_9",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "Oranges_3": {
        "data": "cmap.data._colorbrewer:Oranges_3",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Oranges_4": {
        "data": "cmap.data._colorbrewer:Oranges_4",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Oranges_5": {
        "data": "cmap.data._colorbrewer:Oranges_5",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Oranges_6": {
        "data": "cmap.data._colorbrewer:Oranges_6",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Oranges_7": {
        "data": "cmap.data._colorbrewer:Oranges_7",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Oranges_8": {
        "data": "cmap.data._colorbrewer:Oranges_8",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Oranges_9": {
        "data": "cmap.data._colorbrewer:Oranges_9",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PRGn": {
        "data": "cmap.data._colorbrewer:PRGn_11",
        "category": "diverging",
    },
    "PRGn_10": {
        "data": "cmap.data._colorbrewer:PRGn_10",
        "category": "diverging",
        "interpolation": False,
    },
    "PRGn_11": {
        "data": "cmap.data._colorbrewer:PRGn_11",
        "category": "diverging",
        "interpolation": False,
    },
    "PRGn_3": {
        "data": "cmap.data._colorbrewer:PRGn_3",
        "category": "diverging",
        "interpolation": False,
    },
    "PRGn_4": {
        "data": "cmap.data._colorbrewer:PRGn_4",
        "category": "diverging",
        "interpolation": False,
    },
    "PRGn_5": {
        "data": "cmap.data._colorbrewer:PRGn_5",
        "category": "diverging",
        "interpolation": False,
    },
    "PRGn_6": {
        "data": "cmap.data._colorbrewer:PRGn_6",
        "category": "diverging",
        "interpolation": False,
    },
    "PRGn_7": {
        "data": "cmap.data._colorbrewer:PRGn_7",
        "category": "diverging",
        "interpolation": False,
    },
    "PRGn_8": {
        "data": "cmap.data._colorbrewer:PRGn_8",
        "category": "diverging",
        "interpolation": False,
    },
    "PRGn_9": {
        "data": "cmap.data._colorbrewer:PRGn_9",
        "category": "diverging",
        "interpolation": False,
    },
    "Paired": {
        "data": "cmap.data._colorbrewer:Paired_12",
        "category": "qualitative",
        "interpolation": False,
    },
    "Paired_10": {
        "data": "cmap.data._colorbrewer:Paired_10",
        "category": "qualitative",
        "interpolation": False,
    },
    "Paired_11": {
        "data": "cmap.data._colorbrewer:Paired_11",
        "category": "qualitative",
        "interpolation": False,
    },
    "Paired_12": {
        "data": "cmap.data._colorbrewer:Paired_12",
        "category": "qualitative",
        "interpolation": False,
    },
    "Paired_3": {
        "data": "cmap.data._colorbrewer:Paired_3",
        "category": "qualitative",
        "interpolation": False,
    },
    "Paired_4": {
        "data": "cmap.data._colorbrewer:Paired_4",
        "category": "qualitative",
        "interpolation": False,
    },
    "Paired_5": {
        "data": "cmap.data._colorbrewer:Paired_5",
        "category": "qualitative",
        "interpolation": False,
    },
    "Paired_6": {
        "data": "cmap.data._colorbrewer:Paired_6",
        "category": "qualitative",
        "interpolation": False,
    },
    "Paired_7": {
        "data": "cmap.data._colorbrewer:Paired_7",
        "category": "qualitative",
        "interpolation": False,
    },
    "Paired_8": {
        "data": "cmap.data._colorbrewer:Paired_8",
        "category": "qualitative",
        "interpolation": False,
    },
    "Paired_9": {
        "data": "cmap.data._colorbrewer:Paired_9",
        "category": "qualitative",
        "interpolation": False,
    },
    "Pastel1": {
        "data": "cmap.data._colorbrewer:Pastel1_9",
        "category": "qualitative",
        "interpolation": False,
    },
    "Pastel1_3": {
        "data": "cmap.data._colorbrewer:Pastel1_3",
        "category": "qualitative",
        "interpolation": False,
    },
    "Pastel1_4": {
        "data": "cmap.data._colorbrewer:Pastel1_4",
        "category": "qualitative",
        "interpolation": False,
    },
    "Pastel1_5": {
        "data": "cmap.data._colorbrewer:Pastel1_5",
        "category": "qualitative",
        "interpolation": False,
    },
    "Pastel1_6": {
        "data": "cmap.data._colorbrewer:Pastel1_6",
        "category": "qualitative",
        "interpolation": False,
    },
    "Pastel1_7": {
        "data": "cmap.data._colorbrewer:Pastel1_7",
        "category": "qualitative",
        "interpolation": False,
    },
    "Pastel1_8": {
        "data": "cmap.data._colorbrewer:Pastel1_8",
        "category": "qualitative",
        "interpolation": False,
    },
    "Pastel1_9": {
        "data": "cmap.data._colorbrewer:Pastel1_9",
        "category": "qualitative",
        "interpolation": False,
    },
    "Pastel2": {
        "data": "cmap.data._colorbrewer:Pastel2_8",
        "category": "qualitative",
        "interpolation": False,
    },
    "Pastel2_3": {
        "data": "cmap.data._colorbrewer:Pastel2_3",
        "category": "qualitative",
        "interpolation": False,
    },
    "Pastel2_4": {
        "data": "cmap.data._colorbrewer:Pastel2_4",
        "category": "qualitative",
        "interpolation": False,
    },
    "Pastel2_5": {
        "data": "cmap.data._colorbrewer:Pastel2_5",
        "category": "qualitative",
        "interpolation": False,
    },
    "Pastel2_6": {
        "data": "cmap.data._colorbrewer:Pastel2_6",
        "category": "qualitative",
        "interpolation": False,
    },
    "Pastel2_7": {
        "data": "cmap.data._colorbrewer:Pastel2_7",
        "category": "qualitative",
        "interpolation": False,
    },
    "Pastel2_8": {
        "data": "cmap.data._colorbrewer:Pastel2_8",
        "category": "qualitative",
        "interpolation": False,
    },
    "PiYG": {
        "data": "cmap.data._colorbrewer:PiYG_11",
        "category": "diverging",
    },
    "PiYG_10": {
        "data": "cmap.data._colorbrewer:PiYG_10",
        "category": "diverging",
        "interpolation": False,
    },
    "PiYG_11": {
        "data": "cmap.data._colorbrewer:PiYG_11",
        "category": "diverging",
        "interpolation": False,
    },
    "PiYG_3": {
        "data": "cmap.data._colorbrewer:PiYG_3",
        "category": "diverging",
        "interpolation": False,
    },
    "PiYG_4": {
        "data": "cmap.data._colorbrewer:PiYG_4",
        "category": "diverging",
        "interpolation": False,
    },
    "PiYG_5": {
        "data": "cmap.data._colorbrewer:PiYG_5",
        "category": "diverging",
        "interpolation": False,
    },
    "PiYG_6": {
        "data": "cmap.data._colorbrewer:PiYG_6",
        "category": "diverging",
        "interpolation": False,
    },
    "PiYG_7": {
        "data": "cmap.data._colorbrewer:PiYG_7",
        "category": "diverging",
        "interpolation": False,
    },
    "PiYG_8": {
        "data": "cmap.data._colorbrewer:PiYG_8",
        "category": "diverging",
        "interpolation": False,
    },
    "PiYG_9": {
        "data": "cmap.data._colorbrewer:PiYG_9",
        "category": "diverging",
        "interpolation": False,
    },
    "PuBu": {
        "data": "cmap.data._colorbrewer:PuBu_9",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "PuBuGn": {
        "data": "cmap.data._colorbrewer:PuBuGn_9",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "PuBuGn_3": {
        "data": "cmap.data._colorbrewer:PuBuGn_3",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuBuGn_4": {
        "data": "cmap.data._colorbrewer:PuBuGn_4",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuBuGn_5": {
        "data": "cmap.data._colorbrewer:PuBuGn_5",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuBuGn_6": {
        "data": "cmap.data._colorbrewer:PuBuGn_6",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuBuGn_7": {
        "data": "cmap.data._colorbrewer:PuBuGn_7",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuBuGn_8": {
        "data": "cmap.data._colorbrewer:PuBuGn_8",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuBuGn_9": {
        "data": "cmap.data._colorbrewer:PuBuGn_9",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuBu_3": {
        "data": "cmap.data._colorbrewer:PuBu_3",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuBu_4": {
        "data": "cmap.data._colorbrewer:PuBu_4",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuBu_5": {
        "data": "cmap.data._colorbrewer:PuBu_5",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuBu_6": {
        "data": "cmap.data._colorbrewer:PuBu_6",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuBu_7": {
        "data": "cmap.data._colorbrewer:PuBu_7",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuBu_8": {
        "data": "cmap.data._colorbrewer:PuBu_8",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuBu_9": {
        "data": "cmap.data._colorbrewer:PuBu_9",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuOr": {
        "data": "cmap.data._colorbrewer:PuOr_11",
        "category": "diverging",
    },
    "PuOr_10": {
        "data": "cmap.data._colorbrewer:PuOr_10",
        "category": "diverging",
        "interpolation": False,
    },
    "PuOr_11": {
        "data": "cmap.data._colorbrewer:PuOr_11",
        "category": "diverging",
        "interpolation": False,
    },
    "PuOr_3": {
        "data": "cmap.data._colorbrewer:PuOr_3",
        "category": "diverging",
        "interpolation": False,
    },
    "PuOr_4": {
        "data": "cmap.data._colorbrewer:PuOr_4",
        "category": "diverging",
        "interpolation": False,
    },
    "PuOr_5": {
        "data": "cmap.data._colorbrewer:PuOr_5",
        "category": "diverging",
        "interpolation": False,
    },
    "PuOr_6": {
        "data": "cmap.data._colorbrewer:PuOr_6",
        "category": "diverging",
        "interpolation": False,
    },
    "PuOr_7": {
        "data": "cmap.data._colorbrewer:PuOr_7",
        "category": "diverging",
        "interpolation": False,
    },
    "PuOr_8": {
        "data": "cmap.data._colorbrewer:PuOr_8",
        "category": "diverging",
        "interpolation": False,
    },
    "PuOr_9": {
        "data": "cmap.data._colorbrewer:PuOr_9",
        "category": "diverging",
        "interpolation": False,
    },
    "PuRd": {
        "data": "cmap.data._colorbrewer:PuRd_9",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "PuRd_3": {
        "data": "cmap.data._colorbrewer:PuRd_3",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuRd_4": {
        "data": "cmap.data._colorbrewer:PuRd_4",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuRd_5": {
        "data": "cmap.data._colorbrewer:PuRd_5",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuRd_6": {
        "data": "cmap.data._colorbrewer:PuRd_6",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuRd_7": {
        "data": "cmap.data._colorbrewer:PuRd_7",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuRd_8": {
        "data": "cmap.data._colorbrewer:PuRd_8",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "PuRd_9": {
        "data": "cmap.data._colorbrewer:PuRd_9",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Purples": {
        "data": "cmap.data._colorbrewer:Purples_9",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "Purples_3": {
        "data": "cmap.data._colorbrewer:Purples_3",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Purples_4": {
        "data": "cmap.data._colorbrewer:Purples_4",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Purples_5": {
        "data": "cmap.data._colorbrewer:Purples_5",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Purples_6": {
        "data": "cmap.data._colorbrewer:Purples_6",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Purples_7": {
        "data": "cmap.data._colorbrewer:Purples_7",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Purples_8": {
        "data": "cmap.data._colorbrewer:Purples_8",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Purples_9": {
        "data": "cmap.data._colorbrewer:Purples_9",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "RdBu": {
        "data": "cmap.data._colorbrewer:RdBu_11",
        "category": "diverging",
    },
    "RdBu_10": {
        "data": "cmap.data._colorbrewer:RdBu_10",
        "category": "diverging",
        "interpolation": False,
    },
    "RdBu_11": {
        "data": "cmap.data._colorbrewer:RdBu_11",
        "category": "diverging",
        "interpolation": False,
    },
    "RdBu_3": {
        "data": "cmap.data._colorbrewer:RdBu_3",
        "category": "diverging",
        "interpolation": False,
    },
    "RdBu_4": {
        "data": "cmap.data._colorbrewer:RdBu_4",
        "category": "diverging",
        "interpolation": False,
    },
    "RdBu_5": {
        "data": "cmap.data._colorbrewer:RdBu_5",
        "category": "diverging",
        "interpolation": False,
    },
    "RdBu_6": {
        "data": "cmap.data._colorbrewer:RdBu_6",
        "category": "diverging",
        "interpolation": False,
    },
    "RdBu_7": {
        "data": "cmap.data._colorbrewer:RdBu_7",
        "category": "diverging",
        "interpolation": False,
    },
    "RdBu_8": {
        "data": "cmap.data._colorbrewer:RdBu_8",
        "category": "diverging",
        "interpolation": False,
    },
    "RdBu_9": {
        "data": "cmap.data._colorbrewer:RdBu_9",
        "category": "diverging",
        "interpolation": False,
    },
    "RdGy": {
        "data": "cmap.data._colorbrewer:RdGy_11",
        "category": "diverging",
    },
    "RdGy_10": {
        "data": "cmap.data._colorbrewer:RdGy_10",
        "category": "diverging",
        "interpolation": False,
    },
    "RdGy_11": {
        "data": "cmap.data._colorbrewer:RdGy_11",
        "category": "diverging",
        "interpolation": False,
    },
    "RdGy_3": {
        "data": "cmap.data._colorbrewer:RdGy_3",
        "category": "diverging",
        "interpolation": False,
    },
    "RdGy_4": {
        "data": "cmap.data._colorbrewer:RdGy_4",
        "category": "diverging",
        "interpolation": False,
    },
    "RdGy_5": {
        "data": "cmap.data._colorbrewer:RdGy_5",
        "category": "diverging",
        "interpolation": False,
    },
    "RdGy_6": {
        "data": "cmap.data._colorbrewer:RdGy_6",
        "category": "diverging",
        "interpolation": False,
    },
    "RdGy_7": {
        "data": "cmap.data._colorbrewer:RdGy_7",
        "category": "diverging",
        "interpolation": False,
    },
    "RdGy_8": {
        "data": "cmap.data._colorbrewer:RdGy_8",
        "category": "diverging",
        "interpolation": False,
    },
    "RdGy_9": {
        "data": "cmap.data._colorbrewer:RdGy_9",
        "category": "diverging",
        "interpolation": False,
    },
    "RdPu": {
        "data": "cmap.data._colorbrewer:RdPu_9",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "RdPu_3": {
        "data": "cmap.data._colorbrewer:RdPu_3",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "RdPu_4": {
        "data": "cmap.data._colorbrewer:RdPu_4",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "RdPu_5": {
        "data": "cmap.data._colorbrewer:RdPu_5",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "RdPu_6": {
        "data": "cmap.data._colorbrewer:RdPu_6",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "RdPu_7": {
        "data": "cmap.data._colorbrewer:RdPu_7",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "RdPu_8": {
        "data": "cmap.data._colorbrewer:RdPu_8",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "RdPu_9": {
        "data": "cmap.data._colorbrewer:RdPu_9",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "RdYlBu": {
        "data": "cmap.data._colorbrewer:RdYlBu_11",
        "category": "diverging",
    },
    "RdYlBu_10": {
        "data": "cmap.data._colorbrewer:RdYlBu_10",
        "category": "diverging",
        "interpolation": False,
    },
    "RdYlBu_11": {
        "data": "cmap.data._colorbrewer:RdYlBu_11",
        "category": "diverging",
        "interpolation": False,
    },
    "RdYlBu_3": {
        "data": "cmap.data._colorbrewer:RdYlBu_3",
        "category": "diverging",
        "interpolation": False,
    },
    "RdYlBu_4": {
        "data": "cmap.data._colorbrewer:RdYlBu_4",
        "category": "diverging",
        "interpolation": False,
    },
    "RdYlBu_5": {
        "data": "cmap.data._colorbrewer:RdYlBu_5",
        "category": "diverging",
        "interpolation": False,
    },
    "RdYlBu_6": {
        "data": "cmap.data._colorbrewer:RdYlBu_6",
        "category": "diverging",
        "interpolation": False,
    },
    "RdYlBu_7": {
        "data": "cmap.data._colorbrewer:RdYlBu_7",
        "category": "diverging",
        "interpolation": False,
    },
    "RdYlBu_8": {
        "data": "cmap.data._colorbrewer:RdYlBu_8",
        "category": "diverging",
        "interpolation": False,
    },
    "RdYlBu_9": {
        "data": "cmap.data._colorbrewer:RdYlBu_9",
        "category": "diverging",
        "interpolation": False,
    },
    "RdYlGn": {
        "data": "cmap.data._colorbrewer:RdYlGn_11",
        "category": "diverging",
    },
    "RdYlGn_10": {
        "data": "cmap.data._colorbrewer:RdYlGn_10",
        "category": "diverging",
        "interpolation": False,
    },
    "RdYlGn_11": {
        "data": "cmap.data._colorbrewer:RdYlGn_11",
        "category": "diverging",
        "interpolation": False,
    },
    "RdYlGn_3": {
        "data": "cmap.data._colorbrewer:RdYlGn_3",
        "category": "diverging",
        "interpolation": False,
    },
    "RdYlGn_4": {
        "data": "cmap.data._colorbrewer:RdYlGn_4",
        "category": "diverging",
        "interpolation": False,
    },
    "RdYlGn_5": {
        "data": "cmap.data._colorbrewer:RdYlGn_5",
        "category": "diverging",
        "interpolation": False,
    },
    "RdYlGn_6": {
        "data": "cmap.data._colorbrewer:RdYlGn_6",
        "category": "diverging",
        "interpolation": False,
    },
    "RdYlGn_7": {
        "data": "cmap.data._colorbrewer:RdYlGn_7",
        "category": "diverging",
        "interpolation": False,
    },
    "RdYlGn_8": {
        "data": "cmap.data._colorbrewer:RdYlGn_8",
        "category": "diverging",
        "interpolation": False,
    },
    "RdYlGn_9": {
        "data": "cmap.data._colorbrewer:RdYlGn_9",
        "category": "diverging",
        "interpolation": False,
    },
    "Reds": {
        "data": "cmap.data._colorbrewer:Reds_9",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "Reds_3": {
        "data": "cmap.data._colorbrewer:Reds_3",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Reds_4": {
        "data": "cmap.data._colorbrewer:Reds_4",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Reds_5": {
        "data": "cmap.data._colorbrewer:Reds_5",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Reds_6": {
        "data": "cmap.data._colorbrewer:Reds_6",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Reds_7": {
        "data": "cmap.data._colorbrewer:Reds_7",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Reds_8": {
        "data": "cmap.data._colorbrewer:Reds_8",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Reds_9": {
        "data": "cmap.data._colorbrewer:Reds_9",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "Set1": {
        "data": "cmap.data._colorbrewer:Set1_9",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set1_3": {
        "data": "cmap.data._colorbrewer:Set1_3",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set1_4": {
        "data": "cmap.data._colorbrewer:Set1_4",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set1_5": {
        "data": "cmap.data._colorbrewer:Set1_5",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set1_6": {
        "data": "cmap.data._colorbrewer:Set1_6",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set1_7": {
        "data": "cmap.data._colorbrewer:Set1_7",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set1_8": {
        "data": "cmap.data._colorbrewer:Set1_8",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set1_9": {
        "data": "cmap.data._colorbrewer:Set1_9",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set2": {
        "data": "cmap.data._colorbrewer:Set2_8",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set2_3": {
        "data": "cmap.data._colorbrewer:Set2_3",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set2_4": {
        "data": "cmap.data._colorbrewer:Set2_4",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set2_5": {
        "data": "cmap.data._colorbrewer:Set2_5",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set2_6": {
        "data": "cmap.data._colorbrewer:Set2_6",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set2_7": {
        "data": "cmap.data._colorbrewer:Set2_7",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set2_8": {
        "data": "cmap.data._colorbrewer:Set2_8",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set3": {
        "data": "cmap.data._colorbrewer:Set3_12",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set3_10": {
        "data": "cmap.data._colorbrewer:Set3_10",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set3_11": {
        "data": "cmap.data._colorbrewer:Set3_11",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set3_12": {
        "data": "cmap.data._colorbrewer:Set3_12",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set3_3": {
        "data": "cmap.data._colorbrewer:Set3_3",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set3_4": {
        "data": "cmap.data._colorbrewer:Set3_4",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set3_5": {
        "data": "cmap.data._colorbrewer:Set3_5",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set3_6": {
        "data": "cmap.data._colorbrewer:Set3_6",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set3_7": {
        "data": "cmap.data._colorbrewer:Set3_7",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set3_8": {
        "data": "cmap.data._colorbrewer:Set3_8",
        "category": "qualitative",
        "interpolation": False,
    },
    "Set3_9": {
        "data": "cmap.data._colorbrewer:Set3_9",
        "category": "qualitative",
        "interpolation": False,
    },
    "Spectral": {
        "data": "cmap.data._colorbrewer:Spectral_11",
        "category": "diverging",
    },
    "Spectral_10": {
        "data": "cmap.data._colorbrewer:Spectral_10",
        "category": "diverging",
        "interpolation": False,
    },
    "Spectral_11": {
        "data": "cmap.data._colorbrewer:Spectral_11",
        "category": "diverging",
        "interpolation": False,
    },
    "Spectral_3": {
        "data": "cmap.data._colorbrewer:Spectral_3",
        "category": "diverging",
        "interpolation": False,
    },
    "Spectral_4": {
        "data": "cmap.data._colorbrewer:Spectral_4",
        "category": "diverging",
        "interpolation": False,
    },
    "Spectral_5": {
        "data": "cmap.data._colorbrewer:Spectral_5",
        "category": "diverging",
        "interpolation": False,
    },
    "Spectral_6": {
        "data": "cmap.data._colorbrewer:Spectral_6",
        "category": "diverging",
        "interpolation": False,
    },
    "Spectral_7": {
        "data": "cmap.data._colorbrewer:Spectral_7",
        "category": "diverging",
        "interpolation": False,
    },
    "Spectral_8": {
        "data": "cmap.data._colorbrewer:Spectral_8",
        "category": "diverging",
        "interpolation": False,
    },
    "Spectral_9": {
        "data": "cmap.data._colorbrewer:Spectral_9",
        "category": "diverging",
        "interpolation": False,
    },
    "Wistia": {
        "data": "cmap.data._wistia:Wistia",
        "tags": ["2"],
        "category": "sequential",
    },
    "YlGn": {
        "data": "cmap.data._colorbrewer:YlGn_9",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "YlGnBu": {
        "data": "cmap.data._colorbrewer:YlGnBu_9",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "YlGnBu_3": {
        "data": "cmap.data._colorbrewer:YlGnBu_3",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlGnBu_4": {
        "data": "cmap.data._colorbrewer:YlGnBu_4",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlGnBu_5": {
        "data": "cmap.data._colorbrewer:YlGnBu_5",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlGnBu_6": {
        "data": "cmap.data._colorbrewer:YlGnBu_6",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlGnBu_7": {
        "data": "cmap.data._colorbrewer:YlGnBu_7",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlGnBu_8": {
        "data": "cmap.data._colorbrewer:YlGnBu_8",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlGnBu_9": {
        "data": "cmap.data._colorbrewer:YlGnBu_9",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlGn_3": {
        "data": "cmap.data._colorbrewer:YlGn_3",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlGn_4": {
        "data": "cmap.data._colorbrewer:YlGn_4",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlGn_5": {
        "data": "cmap.data._colorbrewer:YlGn_5",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlGn_6": {
        "data": "cmap.data._colorbrewer:YlGn_6",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlGn_7": {
        "data": "cmap.data._colorbrewer:YlGn_7",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlGn_8": {
        "data": "cmap.data._colorbrewer:YlGn_8",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlGn_9": {
        "data": "cmap.data._colorbrewer:YlGn_9",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlOrBr": {
        "data": "cmap.data._colorbrewer:YlOrBr_9",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "YlOrBr_3": {
        "data": "cmap.data._colorbrewer:YlOrBr_3",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlOrBr_4": {
        "data": "cmap.data._colorbrewer:YlOrBr_4",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlOrBr_5": {
        "data": "cmap.data._colorbrewer:YlOrBr_5",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlOrBr_6": {
        "data": "cmap.data._colorbrewer:YlOrBr_6",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlOrBr_7": {
        "data": "cmap.data._colorbrewer:YlOrBr_7",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlOrBr_8": {
        "data": "cmap.data._colorbrewer:YlOrBr_8",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlOrBr_9": {
        "data": "cmap.data._colorbrewer:YlOrBr_9",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlOrRd": {
        "data": "cmap.data._colorbrewer:YlOrRd_9",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "YlOrRd_3": {
        "data": "cmap.data._colorbrewer:YlOrRd_3",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlOrRd_4": {
        "data": "cmap.data._colorbrewer:YlOrRd_4",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlOrRd_5": {
        "data": "cmap.data._colorbrewer:YlOrRd_5",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlOrRd_6": {
        "data": "cmap.data._colorbrewer:YlOrRd_6",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlOrRd_7": {
        "data": "cmap.data._colorbrewer:YlOrRd_7",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlOrRd_8": {
        "data": "cmap.data._colorbrewer:YlOrRd_8",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "YlOrRd_9": {
        "data": "cmap.data._colorbrewer:YlOrRd_9",
        "tags": ["uniform"],
        "category": "sequential",
        "interpolation": False,
    },
    "afmhot": {
        "data": "cmap.data._gnuplot:afmhot",
        "tags": ["2"],
        "category": "sequential",
    },
    "autumn": {
        "data": "cmap.data._matlab:autumn",
        "tags": ["2"],
        "category": "sequential",
    },
    "binary": {
        "data": "cmap.data._yorik:yarg",
        "tags": ["2"],
        "category": "sequential",
    },
    "blue": {
        "data": "cmap.data._basic_colors:blue",
        "category": "sequential",
    },
    "bone": {"data": "cmap.data._matlab:bone", "tags": ["2"], "category": "sequential"},
    "brg": {
        "data": "cmap.data._matplotlib:brg",
        "category": "miscellaneous",
    },
    "bwr": {"data": "cmap.data._matplotlib:bwr", "category": "diverging"},
    "cividis": {
        "data": "cmap.data._matplotlib:Cividis",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "cool": {"data": "cmap.data._matlab:cool", "tags": ["2"], "category": "sequential"},
    "coolwarm": {
        "data": "cmap.data._moreland:CoolWarm",
        "category": "diverging",
    },
    "copper": {
        "data": "cmap.data._matlab:copper",
        "tags": ["2"],
        "category": "sequential",
    },
    "cubehelix": {
        "data": "cmap.data._cubehelix:cubehelix",
        "category": "miscellaneous",
    },
    "cyan": {
        "data": "cmap.data._basic_colors:cyan",
        "category": "sequential",
    },
    "flag": {"data": "cmap.data._matlab:flag", "category": "miscellaneous"},
    "gist_earth": {
        "data": "cmap.data._yorik:earth",
        "category": "miscellaneous",
    },
    "gist_gray": {
        "data": "cmap.data._gnuplot:gist_gray",
        "tags": ["2"],
        "category": "sequential",
    },
    "gist_heat": {
        "data": "cmap.data._yorik:heat",
        "tags": ["2"],
        "category": "sequential",
    },
    "gist_ncar": {
        "data": "cmap.data._yorik:ncar",
        "category": "miscellaneous",
    },
    "gist_rainbow": {
        "data": "cmap.data._yorik:rainbow",
        "category": "miscellaneous",
    },
    "gist_stern": {
        "data": "cmap.data._yorik:stern",
        "category": "miscellaneous",
    },
    "gist_yarg": {
        "data": "cmap.data._yorik:yarg",
        "tags": ["2"],
        "category": "sequential",
    },
    "gnuplot": {
        "data": "cmap.data._gnuplot:gnuplot",
        "category": "miscellaneous",
    },
    "gnuplot2": {
        "data": "cmap.data._gnuplot:gnuplot2",
        "category": "miscellaneous",
    },
    "gray": {"data": "cmap.data._matlab:gray", "tags": ["2"], "category": "sequential"},
    "grays": {"data": "cmap.data._matlab:gray", "category": "sequential"},
    "green": {
        "data": "cmap.data._basic_colors:green",
        "category": "sequential",
    },
    "hot": {"data": "cmap.data._matlab:hot", "tags": ["2"], "category": "sequential"},
    "hsv": {"data": "cmap.data._matlab:hsv", "category": "cyclic"},
    "inferno": {
        "data": "cmap.data._matplotlib_new:Inferno",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "jet": {"data": "cmap.data._matlab:jet", "category": "miscellaneous"},
    "magenta": {
        "data": "cmap.data._basic_colors:magenta",
        "category": "sequential",
    },
    "magma": {
        "data": "cmap.data._matplotlib_new:Magma",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "nipy_spectral": {
        "data": "cmap.data._nipy:nipy_spectral",
        "category": "miscellaneous",
    },
    "ocean": {
        "data": "cmap.data._gnuplot:ocean",
        "category": "miscellaneous",
    },
    "pink": {"data": "cmap.data._matlab:pink", "tags": ["2"], "category": "sequential"},
    "plasma": {
        "data": "cmap.data._matplotlib_new:Plasma",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "prism": {
        "data": "cmap.data._matlab:prism",
        "category": "miscellaneous",
    },
    "rainbow": {
        "data": "cmap.data._gnuplot:rainbow",
        "category": "miscellaneous",
    },
    "red": {
        "data": "cmap.data._basic_colors:red",
        "category": "sequential",
    },
    "seismic": {
        "data": "cmap.data._matplotlib:seismic",
        "category": "diverging",
    },
    "spring": {
        "data": "cmap.data._matlab:spring",
        "tags": ["2"],
        "category": "sequential",
    },
    "summer": {
        "data": "cmap.data._matlab:summer",
        "tags": ["2"],
        "category": "sequential",
    },
    "tab10": {
        "data": "cmap.data._tableau:Tableau10",
        "category": "qualitative",
        "interpolation": False,
    },
    "tab10_colorblind": {
        "data": "cmap.data._tableau:ColorBlind10",
        "category": "qualitative",
        "interpolation": False,
    },
    "tab10_light": {
        "data": "cmap.data._tableau:Tableau10_Light",
        "category": "qualitative",
        "interpolation": False,
    },
    "tab10_medium": {
        "data": "cmap.data._tableau:Tableau10_Medium",
        "category": "qualitative",
        "interpolation": False,
    },
    "tab20": {
        "data": "cmap.data._tableau:Tableau20",
        "category": "qualitative",
        "interpolation": False,
    },
    "tab20b": {
        "data": "cmap.data._tableau:Tableau20b",
        "category": "qualitative",
        "interpolation": False,
    },
    "tab20c": {
        "data": "cmap.data._tableau:Tableau20c",
        "category": "qualitative",
        "interpolation": False,
    },
    "tab_traffic_light": {
        "data": "cmap.data._tableau:Traffic_Light",
        "category": "qualitative",
        "interpolation": False,
    },
    "terrain": {
        "data": "cmap.data._igor:terrain",
        "category": "miscellaneous",
    },
    "turbo": {
        "data": "cmap.data._turbo:Turbo",
        "category": "miscellaneous",
    },
    "twilight": {
        "data": "cmap.data._matplotlib:Twilight",
        "category": "cyclic",
    },
    "twilight_shifted": {
        "data": "cmap.data._matplotlib:Twilight_shifted",
        "category": "cyclic",
    },
    "viridis": {
        "data": "cmap.data._matplotlib_new:Viridis",
        "tags": ["uniform"],
        "category": "sequential",
    },
    "winter": {
        "data": "cmap.data._matlab:winter",
        "tags": ["2"],
        "category": "sequential",
    },
    "yellow": {
        "data": "cmap.data._basic_colors:yellow",
        "category": "sequential",
    },
    # vispy
    "vispy_light_blues": {
        "data": "cmap.data._vispy:light_blues",
        "category": "sequential",
    },
    "vispy_single_hue": {
        "data": "cmap.data._vispy:single_hue",
        "category": "sequential",
    },
    "vispy_orange": {  # problematic name
        "data": "cmap.data._vispy:orange",
        "category": "sequential",
    },
    "vispy_GrBu": {  # name looks too much like colorbrewer
        "data": "cmap.data._vispy:GrBu",
        "category": "diverging",
    },
    "vispy_GrBu_d": {  # name looks too much like colorbrewer
        "data": "cmap.data._vispy:GrBu_d",
        "category": "diverging",
    },
    "vispy_PuGr": {  # name looks too much like colorbrewer
        "data": "cmap.data._vispy:PuGr",
        "category": "diverging",
    },
    "vispy_RdBu": {
        "data": "cmap.data._vispy:RdBu",
        "category": "diverging",
    },
    "vispy_diverging": {
        "data": "cmap.data._vispy:diverging",
        "category": "diverging",
    },
    "vispy_husl": {
        "data": "cmap.data._vispy:husl",
        "category": "sequential",
    },
    "vispy_hsl": {
        "data": "cmap.data._vispy:hsl",
        "category": "sequential",
    },
    "vispy_fire": {
        "data": "cmap.data._vispy:fire",
        "category": "sequential",
    },
    "vispy_ice": {
        "data": "cmap.data._vispy:ice",
        "category": "sequential",
    },
    "vispy_RdYeBuCy": {
        "data": "cmap.data._vispy:RdYeBuCy",
        "category": "diverging",
    },
    "glasbey": {
        "data": "cmap.data._glasbey:glasbey",
        "category": "qualitative",
        "interpolation": False,
    },
    "imagej_fire": {
        "data": "cmap.data._imagej:Fire",
        "category": "miscellaneous",
    },
    "imagej_ice": {
        "data": "cmap.data._imagej:Ice",
        "category": "miscellaneous",
    },
    "Green_Fire_Blue": {
        "data": "cmap.data._imagej:Green_Fire_Blue",
        "category": "miscellaneous",
    },
    "HiLo": {
        "data": "cmap.data._imagej:HiLo",
        "category": "miscellaneous",
    },
    "algae": {
        "data": "cmap.data._cmocean.algae:algae",
        "category": "sequential",
        "info": "The algae colormap is sequential with whitish-green for low values "
        "and increasing in green with increasing value, which could be used to "
        "represent an increase in chlorophyll in the water. This colormap is based on "
        "[Greens](/catalog/sequential/greens), but was recreated from scratch using "
        "the viscm tool.",
    },
    "amp": {
        "data": "cmap.data._cmocean.amp:amp",
        "category": "sequential",
        "info": "The amp colormap is sequential from whitish to dark red and could be "
        "used to represent an increase in wave height values. This colormap is the "
        "positive half of the [balance](/catalog/diverging/balance) colormap.",
    },
    "balance": {
        "data": "cmap.data._cmocean.balance:balance",
        "category": "diverging",
        "info": "The balance colormap is diverging with dark blue to off-white to dark "
        "red representing negative to zero to positive values; this could be used to "
        "represent sea surface elevation, with deviations in the surface elevations as "
        "shades of color away from neutral off-white. In this case, shades of red have "
        "been chosen to represent sea surface elevation above the reference value "
        "(often mean sea level) to connect with warmer water typically being "
        "associated with an increase in the free surface, such as with the Loop "
        "Current in the Gulf of Mexico. This colormap is based on "
        "[RdBu](/catalog/diverging/RdBu), but was recreated from scratch using the "
        "viscm tool.",
    },
    "balance_blue": {
        "data": "cmap.data._cmocean.balance:balance_blue",
        "category": "sequential",
    },
    "delta": {
        "data": "cmap.data._cmocean.delta:delta",
        "category": "diverging",
        "info": "The delta colormap is diverging from darker blues to just off-white "
        "through shades of yellow green and could be used to represent diverging "
        "velocity values around a critical value (usually zero). This colormap was "
        "inspired by [Francesca Samsel's](http://www.francescasamsel.com/) similar "
        "colormap, but generated from scratch using the viscm tool.",
    },
    "delta_blue": {
        "data": "cmap.data._cmocean.delta:delta_blue",
        "category": "sequential",
    },
    "curl": {
        "data": "cmap.data._cmocean.curl:curl",
        "category": "diverging",
        "info": "The curl colormap is diverging from darker teal to just off-white "
        "through shades of magenta and could be used to represent diverging vorticity "
        "values around a critical value (usually zero).",
    },
    "curl_pink": {
        "data": "cmap.data._cmocean.curl:curl_pink",
        "category": "sequential",
    },
    "diff": {
        "data": "cmap.data._cmocean.diff:diff",
        "category": "diverging",
        "info": "The diff colormap is diverging, with one side shades of blues and one "
        "side shades of browns.",
    },
    "tarn": {
        "data": "cmap.data._cmocean.tarn:tarn",
        "category": "diverging",
        "info": "The tarn colormap is diverging, with one side dry shades of browns "
        "and the other a range of greens and blues. The positive end of the colormap "
        "is meant to reflect the colors in rain and thus be a complementary colormap "
        "to rain for rain anomaly (around 0 or some other critical value).",
    },
    "dense": {
        "data": "cmap.data._cmocean.dense:dense",
        "category": "sequential",
        "info": "The dense colormap is sequential with whitish-blue for low values and "
        "increasing in purple with increasing value, which could be used to represent "
        "an increase in water density. This colormap is based on "
        "[Purples](/catalog/sequential/Purples), but was recreated from scratch using "
        "the viscm tool.",
    },
    "haline": {
        "data": "cmap.data._cmocean.haline:haline",
        "category": "sequential",
        "info": "The haline colormap is sequential, and might be used with dark blue "
        "representing lower salinity or fresher water, transitioning through greens to "
        "light yellow representing increased salinity or saltier water. This colormap "
        "is based on [YlGnBu](/catalog/sequential/YlGnBu/), but was recreated from "
        "scratch using the viscm tool.",
    },
    "ice": {
        "data": "cmap.data._cmocean.ice:ice",
        "category": "sequential",
        "info": "The ice colormap is sequential from very dark blue (almost black) to "
        "very light blue (almost white). A use for this could be representations of "
        "sea ice.",
    },
    "oxy": {
        "data": "cmap.data._cmocean.oxy:oxy",
        "category": "sequential",
        "info": (
            "The oxy colormap is sequential for most of the colormap, representing "
            r"the normal range of oxygen saturation in ocean water, 2and diverging 80% "
            "of the way into the colormap to represent a state of supersaturation. The "
            r"bottom 20% of the colormap is colored reddish to highlight hypoxic or "
            "low oxygen water, but to still print relatively seamlessly into grayscale "
            r"in case the red hue is not important for an application. The top 20% of "
            "the colormap, after the divergence, is colored yellow to highlight the "
            "supersaturated water. The minimum and maximum values of this colormap are "
            "meant to be controlled in order to properly place the low oxygen and "
            "supersaturated oxygen states properly. This colormap was developed for "
            "the Mississippi river plume area where both low and supersaturated "
            "conditions are regularly seen and monitored."
        ),
    },
    "phase": {
        "data": "cmap.data._cmocean.phase:phase",
        "category": "cyclic",
        "info": "The phase colormap is circular, spanning all hues at a set lightness "
        "value. This map is intended to be used for properties such as wave phase and "
        "tidal phase which wrap around from 0˚ to 360˚ to 0˚ and should be represented "
        "without major perceptual jumps in the colormap.",
    },
    "solar": {
        "data": "cmap.data._cmocean.solar:solar",
        "category": "sequential",
        "info": "The solar colormap is sequential from dark brown for low values to "
        "increasingly bright yellow to potentially represent an increase in radiation "
        "in the water.",
    },
    "turbid": {
        "data": "cmap.data._cmocean.turbid:turbid",
        "category": "sequential",
        "info": "The turbid colormap is sequential from light to dark brown and could "
        "be used to represent an increase in sediment in the water.",
    },
    "thermal": {
        "data": "cmap.data._cmocean.thermal:thermal",
        "category": "sequential",
        "info": "The thermal colormap is sequential with dark blue representing lower, "
        "cooler values and transitioning through reds to yellow representing "
        "increased warmer values.",
    },
    "speed": {
        "data": "cmap.data._cmocean.speed:speed",
        "category": "sequential",
        "info": "The speed colormap is sequential from light greenish yellow "
        "representing low values to dark yellowish green representing large values. "
        "This colormap is the positive half of the [delta](/catalog/diverging/delta) "
        "colormap.",
    },
    "deep": {
        "data": "cmap.data._cmocean.deep:deep",
        "category": "sequential",
        "info": "The deep colormap is sequential from light yellow to potentially "
        "represent shallower water through pale green to increasingly dark blue and "
        "purple to represent increasing depth.",
    },
    "matter": {
        "data": "cmap.data._cmocean.matter:matter",
        "category": "sequential",
        "info": "The matter colormap is sequential with whitish-yellow for low values "
        "and increasing in pink with increasing value, and could be used to represent "
        "an increase in material in the water.",
    },
    "tempo": {
        "data": "cmap.data._cmocean.tempo:tempo",
        "category": "sequential",
        "info": "The tempo colormap is sequential from whitish to dark teal and could "
        "be used to represent an increase in wave period values. This colormap is the "
        "negative half of the [curl](/catalog/diverging/curl) colormap.",
    },
    "rain": {
        "data": "cmap.data._cmocean.rain:rain",
        "category": "sequential",
        "info": "The rain colormap is sequential from light, dry colors to blue, wet "
        "colors, and could be used to plot amounts of rainfall.",
    },
    "topo": {
        "data": "cmap.data._cmocean.topo:topo",
        "category": "miscellaneous",
        "info": "The topo colormap has two distinct parts: one that is shades of blue "
        "and yellow to represent water depths (this is the "
        "[deep](/catalog/sequential/deep/) colormap) and one that "
        "is shades of browns and greens to represent land elevation.",
    },
    "rocket": {
        "data": "cmap.data._seaborn:rocket",
        "category": "sequential",
    },
    "mako": {
        "data": "cmap.data._seaborn:mako",
        "category": "sequential",
    },
    "vlag": {
        "data": "cmap.data._seaborn:vlag",
        "category": "diverging",
    },
    "icefire": {
        "data": "cmap.data._seaborn:icefire",
        "category": "diverging",
    },
    "flare": {
        "data": "cmap.data._seaborn:flare",
        "category": "sequential",
    },
    "crest": {
        "data": "cmap.data._seaborn:crest",
        "category": "sequential",
    },
}


def _norm_name(name: str) -> str:
    return name.lower().replace(" ", "_")


_CATALOG_LOWER = {_norm_name(k): v for k, v in CATALOG.items()}


class Catalog(Mapping[str, "LoadedCatalogItem"]):

    _loaded: dict[str, LoadedCatalogItem] = {}

    def __iter__(self) -> Iterator[str]:
        return iter(CATALOG)

    def __len__(self) -> int:
        return len(CATALOG)

    def __getitem__(self, name: str) -> LoadedCatalogItem:
        if name not in self._loaded:
            if (key := _norm_name(name)) not in _CATALOG_LOWER:
                # TODO: print a list of available colormaps or something
                if name != key:
                    raise ValueError(f"Colormap {name!r} (or {key!r}) not found.")
                raise ValueError(f"Colormap {name!r} not found.")

            self._loaded[name] = self._load(key)
            if key != name:
                # cache the requested name as well so we don't need to renormalize
                self._loaded[key] = self._loaded[name]
        return self._loaded[name]

    def _load(self, key: str) -> LoadedCatalogItem:
        """Get the data for a named colormap."""
        item = _CATALOG_LOWER[key].copy()
        # casting here because
        module, attr = item["data"].rsplit(":", 1)
        # not encouraged... but significantly faster than importlib
        # well tested on internal data though
        mod = __import__(module, fromlist=[attr])
        _item = cast("LoadedCatalogItem", item)
        _item.setdefault("source", getattr(mod, "__source__", item["data"]))
        _item["data"] = getattr(mod, attr)
        _item["license"] = mod.__license__  # tests ensure this exists
        _item.setdefault("tags", [])
        _item.setdefault("info", "")
        return _item


catalog = Catalog()
