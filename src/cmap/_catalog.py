"""Colormap catalog.

notes combined from
Peter Kovesi's: https://colorcet.com
mpl docs: https://matplotlib.org/stable/tutorials/colors/colormaps.html#qualitative
colorbrewer2.org: https://colorbrewer2.org

## Sequential

- from maptplotlib docs:
    Sequential change in lightness and often saturation of color incrementally, often
    using a single hue; should be used for representing information that has ordering.

- from colorcet.com:
    Lightness values increase or decrease monotonically/linearly

- from colorbrewer2.org
    Sequential schemes are suited to ordered data that progress from low to high.
    Lightness steps dominate the look of these schemes, with light colors for low data
    values to dark colors for high data values.


## Diverging

- from maptplotlib docs:
    Diverging: change in lightness and possibly saturation of two different colors that
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
    Diverging schemes put equal emphasis on mid-range critical values and extremes at
    both ends of the data range. The critical class or break in the middle of the legend
    is emphasized with light colors and low and high extremes are emphasized with dark
    colors that have contrasting hues.

## Cyclic
- from maptplotlib docs:
    change in lightness of two different colors that meet in the middle and
    beginning/end at an unsaturated color; should be used for values that wrap around at
    the endpoints, such as phase angle, wind direction, or time of day.

- from colorcet.com:
    Have colours that are matched at each end. They are intended for the
    presentation of data that is cyclic such as orientation values or angular phase
    data. They require particular care in their design (the standard colour circle is
    not a good map).


## Qualitative
- from maptplotlib docs:
    Often are miscellaneous colors; should be used to represent information
    which does not have ordering or relationships.

- from colorbrewer2.org
    Qualitative schemes do not imply magnitude differences between legend classes,
    and hues are used to create the primary visual differences between classes.
    Qualitative schemes are best suited to representing nominal or categorical data.


## Miscellaneous

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

from typing import TYPE_CHECKING, Iterator, Literal, cast

if TYPE_CHECKING:
    from typing_extensions import NotRequired, TypeAlias, TypedDict

    from ._colormap import ColorStopsLike

    Category: TypeAlias = Literal[
        "Sequential", "Diverging", "Cyclic", "Qualitative", "Miscellaneous"
    ]

    class CatalogItem(TypedDict):
        data: str
        category: Category
        tags: NotRequired[list[str]]
        interpolation: NotRequired[bool]

    # would be nice to subclass CatalogItem... but can't
    # https://github.com/python/mypy/issues/7435
    class LoadedCatalogItem(TypedDict):
        data: ColorStopsLike
        tags: list[str]
        category: Category
        interpolation: NotRequired[bool]
        license: str
        source: str

    CatalogDict: TypeAlias = dict[str, CatalogItem]

CATALOG: CatalogDict = {
    "Accent": {
        "data": "cmap.data._colorbrewer:Accent_8",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Accent_3": {
        "data": "cmap.data._colorbrewer:Accent_3",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Accent_4": {
        "data": "cmap.data._colorbrewer:Accent_4",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Accent_5": {
        "data": "cmap.data._colorbrewer:Accent_5",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Accent_6": {
        "data": "cmap.data._colorbrewer:Accent_6",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Accent_7": {
        "data": "cmap.data._colorbrewer:Accent_7",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Accent_8": {
        "data": "cmap.data._colorbrewer:Accent_8",
        "category": "Qualitative",
        "interpolation": False,
    },
    "BOP_Blue": {
        "data": "cmap.data._leterrier:BOP_Blue",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "BOP_Orange": {
        "data": "cmap.data._leterrier:BOP_Orange",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "BOP_Purple": {
        "data": "cmap.data._leterrier:BOP_Purple",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "Blues": {
        "data": "cmap.data._colorbrewer:Blues_9",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "Blues_3": {
        "data": "cmap.data._colorbrewer:Blues_3",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Blues_4": {
        "data": "cmap.data._colorbrewer:Blues_4",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Blues_5": {
        "data": "cmap.data._colorbrewer:Blues_5",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Blues_6": {
        "data": "cmap.data._colorbrewer:Blues_6",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Blues_7": {
        "data": "cmap.data._colorbrewer:Blues_7",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Blues_8": {
        "data": "cmap.data._colorbrewer:Blues_8",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Blues_9": {
        "data": "cmap.data._colorbrewer:Blues_9",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "BrBG": {
        "data": "cmap.data._colorbrewer:BrBG_11",
        "category": "Diverging",
    },
    "BrBG_10": {
        "data": "cmap.data._colorbrewer:BrBG_10",
        "category": "Diverging",
        "interpolation": False,
    },
    "BrBG_11": {
        "data": "cmap.data._colorbrewer:BrBG_11",
        "category": "Diverging",
        "interpolation": False,
    },
    "BrBG_3": {
        "data": "cmap.data._colorbrewer:BrBG_3",
        "category": "Diverging",
        "interpolation": False,
    },
    "BrBG_4": {
        "data": "cmap.data._colorbrewer:BrBG_4",
        "category": "Diverging",
        "interpolation": False,
    },
    "BrBG_5": {
        "data": "cmap.data._colorbrewer:BrBG_5",
        "category": "Diverging",
        "interpolation": False,
    },
    "BrBG_6": {
        "data": "cmap.data._colorbrewer:BrBG_6",
        "category": "Diverging",
        "interpolation": False,
    },
    "BrBG_7": {
        "data": "cmap.data._colorbrewer:BrBG_7",
        "category": "Diverging",
        "interpolation": False,
    },
    "BrBG_8": {
        "data": "cmap.data._colorbrewer:BrBG_8",
        "category": "Diverging",
        "interpolation": False,
    },
    "BrBG_9": {
        "data": "cmap.data._colorbrewer:BrBG_9",
        "category": "Diverging",
        "interpolation": False,
    },
    "BuGn": {
        "data": "cmap.data._colorbrewer:BuGn_9",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "BuGn_3": {
        "data": "cmap.data._colorbrewer:BuGn_3",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "BuGn_4": {
        "data": "cmap.data._colorbrewer:BuGn_4",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "BuGn_5": {
        "data": "cmap.data._colorbrewer:BuGn_5",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "BuGn_6": {
        "data": "cmap.data._colorbrewer:BuGn_6",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "BuGn_7": {
        "data": "cmap.data._colorbrewer:BuGn_7",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "BuGn_8": {
        "data": "cmap.data._colorbrewer:BuGn_8",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "BuGn_9": {
        "data": "cmap.data._colorbrewer:BuGn_9",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "BuPu": {
        "data": "cmap.data._colorbrewer:BuPu_9",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "BuPu_3": {
        "data": "cmap.data._colorbrewer:BuPu_3",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "BuPu_4": {
        "data": "cmap.data._colorbrewer:BuPu_4",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "BuPu_5": {
        "data": "cmap.data._colorbrewer:BuPu_5",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "BuPu_6": {
        "data": "cmap.data._colorbrewer:BuPu_6",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "BuPu_7": {
        "data": "cmap.data._colorbrewer:BuPu_7",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "BuPu_8": {
        "data": "cmap.data._colorbrewer:BuPu_8",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "BuPu_9": {
        "data": "cmap.data._colorbrewer:BuPu_9",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "CMRmap": {
        "data": "cmap.data._CMRmap:CMRmap",
        "category": "Miscellaneous",
    },
    "Dark2": {
        "data": "cmap.data._colorbrewer:Dark2_8",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Dark2_3": {
        "data": "cmap.data._colorbrewer:Dark2_3",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Dark2_4": {
        "data": "cmap.data._colorbrewer:Dark2_4",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Dark2_5": {
        "data": "cmap.data._colorbrewer:Dark2_5",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Dark2_6": {
        "data": "cmap.data._colorbrewer:Dark2_6",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Dark2_7": {
        "data": "cmap.data._colorbrewer:Dark2_7",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Dark2_8": {
        "data": "cmap.data._colorbrewer:Dark2_8",
        "category": "Qualitative",
        "interpolation": False,
    },
    "GnBu": {
        "data": "cmap.data._colorbrewer:GnBu_9",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "GnBu_3": {
        "data": "cmap.data._colorbrewer:GnBu_3",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "GnBu_4": {
        "data": "cmap.data._colorbrewer:GnBu_4",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "GnBu_5": {
        "data": "cmap.data._colorbrewer:GnBu_5",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "GnBu_6": {
        "data": "cmap.data._colorbrewer:GnBu_6",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "GnBu_7": {
        "data": "cmap.data._colorbrewer:GnBu_7",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "GnBu_8": {
        "data": "cmap.data._colorbrewer:GnBu_8",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "GnBu_9": {
        "data": "cmap.data._colorbrewer:GnBu_9",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Greens": {
        "data": "cmap.data._colorbrewer:Greens_9",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "Greens_3": {
        "data": "cmap.data._colorbrewer:Greens_3",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Greens_4": {
        "data": "cmap.data._colorbrewer:Greens_4",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Greens_5": {
        "data": "cmap.data._colorbrewer:Greens_5",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Greens_6": {
        "data": "cmap.data._colorbrewer:Greens_6",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Greens_7": {
        "data": "cmap.data._colorbrewer:Greens_7",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Greens_8": {
        "data": "cmap.data._colorbrewer:Greens_8",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Greens_9": {
        "data": "cmap.data._colorbrewer:Greens_9",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Greys": {
        "data": "cmap.data._colorbrewer:Greys_9",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "Greys_3": {
        "data": "cmap.data._colorbrewer:Greys_3",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Greys_4": {
        "data": "cmap.data._colorbrewer:Greys_4",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Greys_5": {
        "data": "cmap.data._colorbrewer:Greys_5",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Greys_6": {
        "data": "cmap.data._colorbrewer:Greys_6",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Greys_7": {
        "data": "cmap.data._colorbrewer:Greys_7",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Greys_8": {
        "data": "cmap.data._colorbrewer:Greys_8",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Greys_9": {
        "data": "cmap.data._colorbrewer:Greys_9",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "I_Blue": {
        "data": "cmap.data._leterrier:I_Blue",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "I_Bordeaux": {
        "data": "cmap.data._leterrier:I_Bordeaux",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "I_Cyan": {
        "data": "cmap.data._leterrier:I_Cyan",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "I_Forest": {
        "data": "cmap.data._leterrier:I_Forest",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "I_Green": {
        "data": "cmap.data._leterrier:I_Green",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "I_Magenta": {
        "data": "cmap.data._leterrier:I_Magenta",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "I_Orange": {
        "data": "cmap.data._leterrier:I_Orange",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "I_Purple": {
        "data": "cmap.data._leterrier:I_Purple",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "I_Red": {
        "data": "cmap.data._leterrier:I_Red",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "I_Yellow": {
        "data": "cmap.data._leterrier:I_Yellow",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "OrRd": {
        "data": "cmap.data._colorbrewer:OrRd_9",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "OrRd_3": {
        "data": "cmap.data._colorbrewer:OrRd_3",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "OrRd_4": {
        "data": "cmap.data._colorbrewer:OrRd_4",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "OrRd_5": {
        "data": "cmap.data._colorbrewer:OrRd_5",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "OrRd_6": {
        "data": "cmap.data._colorbrewer:OrRd_6",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "OrRd_7": {
        "data": "cmap.data._colorbrewer:OrRd_7",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "OrRd_8": {
        "data": "cmap.data._colorbrewer:OrRd_8",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "OrRd_9": {
        "data": "cmap.data._colorbrewer:OrRd_9",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Oranges": {
        "data": "cmap.data._colorbrewer:Oranges_9",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "Oranges_3": {
        "data": "cmap.data._colorbrewer:Oranges_3",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Oranges_4": {
        "data": "cmap.data._colorbrewer:Oranges_4",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Oranges_5": {
        "data": "cmap.data._colorbrewer:Oranges_5",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Oranges_6": {
        "data": "cmap.data._colorbrewer:Oranges_6",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Oranges_7": {
        "data": "cmap.data._colorbrewer:Oranges_7",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Oranges_8": {
        "data": "cmap.data._colorbrewer:Oranges_8",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Oranges_9": {
        "data": "cmap.data._colorbrewer:Oranges_9",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PRGn": {
        "data": "cmap.data._colorbrewer:PRGn_11",
        "category": "Diverging",
    },
    "PRGn_10": {
        "data": "cmap.data._colorbrewer:PRGn_10",
        "category": "Diverging",
        "interpolation": False,
    },
    "PRGn_11": {
        "data": "cmap.data._colorbrewer:PRGn_11",
        "category": "Diverging",
        "interpolation": False,
    },
    "PRGn_3": {
        "data": "cmap.data._colorbrewer:PRGn_3",
        "category": "Diverging",
        "interpolation": False,
    },
    "PRGn_4": {
        "data": "cmap.data._colorbrewer:PRGn_4",
        "category": "Diverging",
        "interpolation": False,
    },
    "PRGn_5": {
        "data": "cmap.data._colorbrewer:PRGn_5",
        "category": "Diverging",
        "interpolation": False,
    },
    "PRGn_6": {
        "data": "cmap.data._colorbrewer:PRGn_6",
        "category": "Diverging",
        "interpolation": False,
    },
    "PRGn_7": {
        "data": "cmap.data._colorbrewer:PRGn_7",
        "category": "Diverging",
        "interpolation": False,
    },
    "PRGn_8": {
        "data": "cmap.data._colorbrewer:PRGn_8",
        "category": "Diverging",
        "interpolation": False,
    },
    "PRGn_9": {
        "data": "cmap.data._colorbrewer:PRGn_9",
        "category": "Diverging",
        "interpolation": False,
    },
    "Paired": {
        "data": "cmap.data._colorbrewer:Paired_12",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Paired_10": {
        "data": "cmap.data._colorbrewer:Paired_10",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Paired_11": {
        "data": "cmap.data._colorbrewer:Paired_11",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Paired_12": {
        "data": "cmap.data._colorbrewer:Paired_12",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Paired_3": {
        "data": "cmap.data._colorbrewer:Paired_3",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Paired_4": {
        "data": "cmap.data._colorbrewer:Paired_4",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Paired_5": {
        "data": "cmap.data._colorbrewer:Paired_5",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Paired_6": {
        "data": "cmap.data._colorbrewer:Paired_6",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Paired_7": {
        "data": "cmap.data._colorbrewer:Paired_7",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Paired_8": {
        "data": "cmap.data._colorbrewer:Paired_8",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Paired_9": {
        "data": "cmap.data._colorbrewer:Paired_9",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Pastel1": {
        "data": "cmap.data._colorbrewer:Pastel1_9",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Pastel1_3": {
        "data": "cmap.data._colorbrewer:Pastel1_3",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Pastel1_4": {
        "data": "cmap.data._colorbrewer:Pastel1_4",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Pastel1_5": {
        "data": "cmap.data._colorbrewer:Pastel1_5",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Pastel1_6": {
        "data": "cmap.data._colorbrewer:Pastel1_6",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Pastel1_7": {
        "data": "cmap.data._colorbrewer:Pastel1_7",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Pastel1_8": {
        "data": "cmap.data._colorbrewer:Pastel1_8",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Pastel1_9": {
        "data": "cmap.data._colorbrewer:Pastel1_9",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Pastel2": {
        "data": "cmap.data._colorbrewer:Pastel2_8",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Pastel2_3": {
        "data": "cmap.data._colorbrewer:Pastel2_3",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Pastel2_4": {
        "data": "cmap.data._colorbrewer:Pastel2_4",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Pastel2_5": {
        "data": "cmap.data._colorbrewer:Pastel2_5",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Pastel2_6": {
        "data": "cmap.data._colorbrewer:Pastel2_6",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Pastel2_7": {
        "data": "cmap.data._colorbrewer:Pastel2_7",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Pastel2_8": {
        "data": "cmap.data._colorbrewer:Pastel2_8",
        "category": "Qualitative",
        "interpolation": False,
    },
    "PiYG": {
        "data": "cmap.data._colorbrewer:PiYG_11",
        "category": "Diverging",
    },
    "PiYG_10": {
        "data": "cmap.data._colorbrewer:PiYG_10",
        "category": "Diverging",
        "interpolation": False,
    },
    "PiYG_11": {
        "data": "cmap.data._colorbrewer:PiYG_11",
        "category": "Diverging",
        "interpolation": False,
    },
    "PiYG_3": {
        "data": "cmap.data._colorbrewer:PiYG_3",
        "category": "Diverging",
        "interpolation": False,
    },
    "PiYG_4": {
        "data": "cmap.data._colorbrewer:PiYG_4",
        "category": "Diverging",
        "interpolation": False,
    },
    "PiYG_5": {
        "data": "cmap.data._colorbrewer:PiYG_5",
        "category": "Diverging",
        "interpolation": False,
    },
    "PiYG_6": {
        "data": "cmap.data._colorbrewer:PiYG_6",
        "category": "Diverging",
        "interpolation": False,
    },
    "PiYG_7": {
        "data": "cmap.data._colorbrewer:PiYG_7",
        "category": "Diverging",
        "interpolation": False,
    },
    "PiYG_8": {
        "data": "cmap.data._colorbrewer:PiYG_8",
        "category": "Diverging",
        "interpolation": False,
    },
    "PiYG_9": {
        "data": "cmap.data._colorbrewer:PiYG_9",
        "category": "Diverging",
        "interpolation": False,
    },
    "PuBu": {
        "data": "cmap.data._colorbrewer:PuBu_9",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "PuBuGn": {
        "data": "cmap.data._colorbrewer:PuBuGn_9",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "PuBuGn_3": {
        "data": "cmap.data._colorbrewer:PuBuGn_3",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuBuGn_4": {
        "data": "cmap.data._colorbrewer:PuBuGn_4",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuBuGn_5": {
        "data": "cmap.data._colorbrewer:PuBuGn_5",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuBuGn_6": {
        "data": "cmap.data._colorbrewer:PuBuGn_6",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuBuGn_7": {
        "data": "cmap.data._colorbrewer:PuBuGn_7",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuBuGn_8": {
        "data": "cmap.data._colorbrewer:PuBuGn_8",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuBuGn_9": {
        "data": "cmap.data._colorbrewer:PuBuGn_9",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuBu_3": {
        "data": "cmap.data._colorbrewer:PuBu_3",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuBu_4": {
        "data": "cmap.data._colorbrewer:PuBu_4",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuBu_5": {
        "data": "cmap.data._colorbrewer:PuBu_5",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuBu_6": {
        "data": "cmap.data._colorbrewer:PuBu_6",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuBu_7": {
        "data": "cmap.data._colorbrewer:PuBu_7",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuBu_8": {
        "data": "cmap.data._colorbrewer:PuBu_8",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuBu_9": {
        "data": "cmap.data._colorbrewer:PuBu_9",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuOr": {
        "data": "cmap.data._colorbrewer:PuOr_11",
        "category": "Diverging",
    },
    "PuOr_10": {
        "data": "cmap.data._colorbrewer:PuOr_10",
        "category": "Diverging",
        "interpolation": False,
    },
    "PuOr_11": {
        "data": "cmap.data._colorbrewer:PuOr_11",
        "category": "Diverging",
        "interpolation": False,
    },
    "PuOr_3": {
        "data": "cmap.data._colorbrewer:PuOr_3",
        "category": "Diverging",
        "interpolation": False,
    },
    "PuOr_4": {
        "data": "cmap.data._colorbrewer:PuOr_4",
        "category": "Diverging",
        "interpolation": False,
    },
    "PuOr_5": {
        "data": "cmap.data._colorbrewer:PuOr_5",
        "category": "Diverging",
        "interpolation": False,
    },
    "PuOr_6": {
        "data": "cmap.data._colorbrewer:PuOr_6",
        "category": "Diverging",
        "interpolation": False,
    },
    "PuOr_7": {
        "data": "cmap.data._colorbrewer:PuOr_7",
        "category": "Diverging",
        "interpolation": False,
    },
    "PuOr_8": {
        "data": "cmap.data._colorbrewer:PuOr_8",
        "category": "Diverging",
        "interpolation": False,
    },
    "PuOr_9": {
        "data": "cmap.data._colorbrewer:PuOr_9",
        "category": "Diverging",
        "interpolation": False,
    },
    "PuRd": {
        "data": "cmap.data._colorbrewer:PuRd_9",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "PuRd_3": {
        "data": "cmap.data._colorbrewer:PuRd_3",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuRd_4": {
        "data": "cmap.data._colorbrewer:PuRd_4",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuRd_5": {
        "data": "cmap.data._colorbrewer:PuRd_5",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuRd_6": {
        "data": "cmap.data._colorbrewer:PuRd_6",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuRd_7": {
        "data": "cmap.data._colorbrewer:PuRd_7",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuRd_8": {
        "data": "cmap.data._colorbrewer:PuRd_8",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "PuRd_9": {
        "data": "cmap.data._colorbrewer:PuRd_9",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Purples": {
        "data": "cmap.data._colorbrewer:Purples_9",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "Purples_3": {
        "data": "cmap.data._colorbrewer:Purples_3",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Purples_4": {
        "data": "cmap.data._colorbrewer:Purples_4",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Purples_5": {
        "data": "cmap.data._colorbrewer:Purples_5",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Purples_6": {
        "data": "cmap.data._colorbrewer:Purples_6",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Purples_7": {
        "data": "cmap.data._colorbrewer:Purples_7",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Purples_8": {
        "data": "cmap.data._colorbrewer:Purples_8",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Purples_9": {
        "data": "cmap.data._colorbrewer:Purples_9",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "RdBu": {
        "data": "cmap.data._colorbrewer:RdBu_11",
        "category": "Diverging",
    },
    "RdBu_10": {
        "data": "cmap.data._colorbrewer:RdBu_10",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdBu_11": {
        "data": "cmap.data._colorbrewer:RdBu_11",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdBu_3": {
        "data": "cmap.data._colorbrewer:RdBu_3",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdBu_4": {
        "data": "cmap.data._colorbrewer:RdBu_4",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdBu_5": {
        "data": "cmap.data._colorbrewer:RdBu_5",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdBu_6": {
        "data": "cmap.data._colorbrewer:RdBu_6",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdBu_7": {
        "data": "cmap.data._colorbrewer:RdBu_7",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdBu_8": {
        "data": "cmap.data._colorbrewer:RdBu_8",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdBu_9": {
        "data": "cmap.data._colorbrewer:RdBu_9",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdGy": {
        "data": "cmap.data._colorbrewer:RdGy_11",
        "category": "Diverging",
    },
    "RdGy_10": {
        "data": "cmap.data._colorbrewer:RdGy_10",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdGy_11": {
        "data": "cmap.data._colorbrewer:RdGy_11",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdGy_3": {
        "data": "cmap.data._colorbrewer:RdGy_3",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdGy_4": {
        "data": "cmap.data._colorbrewer:RdGy_4",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdGy_5": {
        "data": "cmap.data._colorbrewer:RdGy_5",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdGy_6": {
        "data": "cmap.data._colorbrewer:RdGy_6",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdGy_7": {
        "data": "cmap.data._colorbrewer:RdGy_7",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdGy_8": {
        "data": "cmap.data._colorbrewer:RdGy_8",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdGy_9": {
        "data": "cmap.data._colorbrewer:RdGy_9",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdPu": {
        "data": "cmap.data._colorbrewer:RdPu_9",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "RdPu_3": {
        "data": "cmap.data._colorbrewer:RdPu_3",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "RdPu_4": {
        "data": "cmap.data._colorbrewer:RdPu_4",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "RdPu_5": {
        "data": "cmap.data._colorbrewer:RdPu_5",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "RdPu_6": {
        "data": "cmap.data._colorbrewer:RdPu_6",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "RdPu_7": {
        "data": "cmap.data._colorbrewer:RdPu_7",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "RdPu_8": {
        "data": "cmap.data._colorbrewer:RdPu_8",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "RdPu_9": {
        "data": "cmap.data._colorbrewer:RdPu_9",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "RdYlBu": {
        "data": "cmap.data._colorbrewer:RdYlBu_11",
        "category": "Diverging",
    },
    "RdYlBu_10": {
        "data": "cmap.data._colorbrewer:RdYlBu_10",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdYlBu_11": {
        "data": "cmap.data._colorbrewer:RdYlBu_11",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdYlBu_3": {
        "data": "cmap.data._colorbrewer:RdYlBu_3",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdYlBu_4": {
        "data": "cmap.data._colorbrewer:RdYlBu_4",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdYlBu_5": {
        "data": "cmap.data._colorbrewer:RdYlBu_5",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdYlBu_6": {
        "data": "cmap.data._colorbrewer:RdYlBu_6",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdYlBu_7": {
        "data": "cmap.data._colorbrewer:RdYlBu_7",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdYlBu_8": {
        "data": "cmap.data._colorbrewer:RdYlBu_8",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdYlBu_9": {
        "data": "cmap.data._colorbrewer:RdYlBu_9",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdYlGn": {
        "data": "cmap.data._colorbrewer:RdYlGn_11",
        "category": "Diverging",
    },
    "RdYlGn_10": {
        "data": "cmap.data._colorbrewer:RdYlGn_10",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdYlGn_11": {
        "data": "cmap.data._colorbrewer:RdYlGn_11",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdYlGn_3": {
        "data": "cmap.data._colorbrewer:RdYlGn_3",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdYlGn_4": {
        "data": "cmap.data._colorbrewer:RdYlGn_4",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdYlGn_5": {
        "data": "cmap.data._colorbrewer:RdYlGn_5",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdYlGn_6": {
        "data": "cmap.data._colorbrewer:RdYlGn_6",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdYlGn_7": {
        "data": "cmap.data._colorbrewer:RdYlGn_7",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdYlGn_8": {
        "data": "cmap.data._colorbrewer:RdYlGn_8",
        "category": "Diverging",
        "interpolation": False,
    },
    "RdYlGn_9": {
        "data": "cmap.data._colorbrewer:RdYlGn_9",
        "category": "Diverging",
        "interpolation": False,
    },
    "Reds": {
        "data": "cmap.data._colorbrewer:Reds_9",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "Reds_3": {
        "data": "cmap.data._colorbrewer:Reds_3",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Reds_4": {
        "data": "cmap.data._colorbrewer:Reds_4",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Reds_5": {
        "data": "cmap.data._colorbrewer:Reds_5",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Reds_6": {
        "data": "cmap.data._colorbrewer:Reds_6",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Reds_7": {
        "data": "cmap.data._colorbrewer:Reds_7",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Reds_8": {
        "data": "cmap.data._colorbrewer:Reds_8",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Reds_9": {
        "data": "cmap.data._colorbrewer:Reds_9",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "Set1": {
        "data": "cmap.data._colorbrewer:Set1_9",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set1_3": {
        "data": "cmap.data._colorbrewer:Set1_3",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set1_4": {
        "data": "cmap.data._colorbrewer:Set1_4",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set1_5": {
        "data": "cmap.data._colorbrewer:Set1_5",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set1_6": {
        "data": "cmap.data._colorbrewer:Set1_6",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set1_7": {
        "data": "cmap.data._colorbrewer:Set1_7",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set1_8": {
        "data": "cmap.data._colorbrewer:Set1_8",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set1_9": {
        "data": "cmap.data._colorbrewer:Set1_9",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set2": {
        "data": "cmap.data._colorbrewer:Set2_8",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set2_3": {
        "data": "cmap.data._colorbrewer:Set2_3",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set2_4": {
        "data": "cmap.data._colorbrewer:Set2_4",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set2_5": {
        "data": "cmap.data._colorbrewer:Set2_5",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set2_6": {
        "data": "cmap.data._colorbrewer:Set2_6",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set2_7": {
        "data": "cmap.data._colorbrewer:Set2_7",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set2_8": {
        "data": "cmap.data._colorbrewer:Set2_8",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set3": {
        "data": "cmap.data._colorbrewer:Set3_12",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set3_10": {
        "data": "cmap.data._colorbrewer:Set3_10",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set3_11": {
        "data": "cmap.data._colorbrewer:Set3_11",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set3_12": {
        "data": "cmap.data._colorbrewer:Set3_12",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set3_3": {
        "data": "cmap.data._colorbrewer:Set3_3",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set3_4": {
        "data": "cmap.data._colorbrewer:Set3_4",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set3_5": {
        "data": "cmap.data._colorbrewer:Set3_5",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set3_6": {
        "data": "cmap.data._colorbrewer:Set3_6",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set3_7": {
        "data": "cmap.data._colorbrewer:Set3_7",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set3_8": {
        "data": "cmap.data._colorbrewer:Set3_8",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Set3_9": {
        "data": "cmap.data._colorbrewer:Set3_9",
        "category": "Qualitative",
        "interpolation": False,
    },
    "Spectral": {
        "data": "cmap.data._colorbrewer:Spectral_11",
        "category": "Diverging",
    },
    "Spectral_10": {
        "data": "cmap.data._colorbrewer:Spectral_10",
        "category": "Diverging",
        "interpolation": False,
    },
    "Spectral_11": {
        "data": "cmap.data._colorbrewer:Spectral_11",
        "category": "Diverging",
        "interpolation": False,
    },
    "Spectral_3": {
        "data": "cmap.data._colorbrewer:Spectral_3",
        "category": "Diverging",
        "interpolation": False,
    },
    "Spectral_4": {
        "data": "cmap.data._colorbrewer:Spectral_4",
        "category": "Diverging",
        "interpolation": False,
    },
    "Spectral_5": {
        "data": "cmap.data._colorbrewer:Spectral_5",
        "category": "Diverging",
        "interpolation": False,
    },
    "Spectral_6": {
        "data": "cmap.data._colorbrewer:Spectral_6",
        "category": "Diverging",
        "interpolation": False,
    },
    "Spectral_7": {
        "data": "cmap.data._colorbrewer:Spectral_7",
        "category": "Diverging",
        "interpolation": False,
    },
    "Spectral_8": {
        "data": "cmap.data._colorbrewer:Spectral_8",
        "category": "Diverging",
        "interpolation": False,
    },
    "Spectral_9": {
        "data": "cmap.data._colorbrewer:Spectral_9",
        "category": "Diverging",
        "interpolation": False,
    },
    "Wistia": {
        "data": "cmap.data._wistia:Wistia",
        "tags": ["2"],
        "category": "Sequential",
    },
    "YlGn": {
        "data": "cmap.data._colorbrewer:YlGn_9",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "YlGnBu": {
        "data": "cmap.data._colorbrewer:YlGnBu_9",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "YlGnBu_3": {
        "data": "cmap.data._colorbrewer:YlGnBu_3",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlGnBu_4": {
        "data": "cmap.data._colorbrewer:YlGnBu_4",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlGnBu_5": {
        "data": "cmap.data._colorbrewer:YlGnBu_5",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlGnBu_6": {
        "data": "cmap.data._colorbrewer:YlGnBu_6",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlGnBu_7": {
        "data": "cmap.data._colorbrewer:YlGnBu_7",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlGnBu_8": {
        "data": "cmap.data._colorbrewer:YlGnBu_8",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlGnBu_9": {
        "data": "cmap.data._colorbrewer:YlGnBu_9",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlGn_3": {
        "data": "cmap.data._colorbrewer:YlGn_3",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlGn_4": {
        "data": "cmap.data._colorbrewer:YlGn_4",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlGn_5": {
        "data": "cmap.data._colorbrewer:YlGn_5",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlGn_6": {
        "data": "cmap.data._colorbrewer:YlGn_6",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlGn_7": {
        "data": "cmap.data._colorbrewer:YlGn_7",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlGn_8": {
        "data": "cmap.data._colorbrewer:YlGn_8",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlGn_9": {
        "data": "cmap.data._colorbrewer:YlGn_9",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlOrBr": {
        "data": "cmap.data._colorbrewer:YlOrBr_9",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "YlOrBr_3": {
        "data": "cmap.data._colorbrewer:YlOrBr_3",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlOrBr_4": {
        "data": "cmap.data._colorbrewer:YlOrBr_4",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlOrBr_5": {
        "data": "cmap.data._colorbrewer:YlOrBr_5",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlOrBr_6": {
        "data": "cmap.data._colorbrewer:YlOrBr_6",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlOrBr_7": {
        "data": "cmap.data._colorbrewer:YlOrBr_7",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlOrBr_8": {
        "data": "cmap.data._colorbrewer:YlOrBr_8",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlOrBr_9": {
        "data": "cmap.data._colorbrewer:YlOrBr_9",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlOrRd": {
        "data": "cmap.data._colorbrewer:YlOrRd_9",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "YlOrRd_3": {
        "data": "cmap.data._colorbrewer:YlOrRd_3",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlOrRd_4": {
        "data": "cmap.data._colorbrewer:YlOrRd_4",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlOrRd_5": {
        "data": "cmap.data._colorbrewer:YlOrRd_5",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlOrRd_6": {
        "data": "cmap.data._colorbrewer:YlOrRd_6",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlOrRd_7": {
        "data": "cmap.data._colorbrewer:YlOrRd_7",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlOrRd_8": {
        "data": "cmap.data._colorbrewer:YlOrRd_8",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "YlOrRd_9": {
        "data": "cmap.data._colorbrewer:YlOrRd_9",
        "tags": ["uniform"],
        "category": "Sequential",
        "interpolation": False,
    },
    "afmhot": {
        "data": "cmap.data._gnuplot:afmhot",
        "tags": ["2"],
        "category": "Sequential",
    },
    "autumn": {
        "data": "cmap.data._matlab:autumn",
        "tags": ["2"],
        "category": "Sequential",
    },
    "binary": {
        "data": "cmap.data._yorik:yarg",
        "tags": ["2"],
        "category": "Sequential",
    },
    "blue": {
        "data": "cmap.data._basic_colors:blue",
        "category": "Sequential",
    },
    "bone": {"data": "cmap.data._matlab:bone", "tags": ["2"], "category": "Sequential"},
    "brg": {
        "data": "cmap.data._matplotlib:brg",
        "category": "Miscellaneous",
    },
    "bwr": {"data": "cmap.data._matplotlib:bwr", "category": "Diverging"},
    "cividis": {
        "data": "cmap.data._matplotlib:Cividis",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "cool": {"data": "cmap.data._matlab:cool", "tags": ["2"], "category": "Sequential"},
    "coolwarm": {
        "data": "cmap.data._moreland:CoolWarm",
        "category": "Diverging",
    },
    "copper": {
        "data": "cmap.data._matlab:copper",
        "tags": ["2"],
        "category": "Sequential",
    },
    "cubehelix": {
        "data": "cmap.data._cubehelix:cubehelix",
        "category": "Miscellaneous",
    },
    "cyan": {
        "data": "cmap.data._basic_colors:cyan",
        "category": "Sequential",
    },
    "flag": {"data": "cmap.data._matlab:flag", "category": "Miscellaneous"},
    "gist_earth": {
        "data": "cmap.data._yorik:earth",
        "category": "Miscellaneous",
    },
    "gist_gray": {
        "data": "cmap.data._gnuplot:gist_gray",
        "tags": ["2"],
        "category": "Sequential",
    },
    "gist_heat": {
        "data": "cmap.data._yorik:heat",
        "tags": ["2"],
        "category": "Sequential",
    },
    "gist_ncar": {
        "data": "cmap.data._yorik:ncar",
        "category": "Miscellaneous",
    },
    "gist_rainbow": {
        "data": "cmap.data._yorik:rainbow",
        "category": "Miscellaneous",
    },
    "gist_stern": {
        "data": "cmap.data._yorik:stern",
        "category": "Miscellaneous",
    },
    "gist_yarg": {
        "data": "cmap.data._yorik:yarg",
        "tags": ["2"],
        "category": "Sequential",
    },
    "gnuplot": {
        "data": "cmap.data._gnuplot:gnuplot",
        "category": "Miscellaneous",
    },
    "gnuplot2": {
        "data": "cmap.data._gnuplot:gnuplot2",
        "category": "Miscellaneous",
    },
    "gray": {"data": "cmap.data._matlab:gray", "tags": ["2"], "category": "Sequential"},
    "grays": {"data": "cmap.data._matlab:gray", "category": "Sequential"},
    "green": {
        "data": "cmap.data._basic_colors:green",
        "category": "Sequential",
    },
    "hot": {"data": "cmap.data._matlab:hot", "tags": ["2"], "category": "Sequential"},
    "hsv": {"data": "cmap.data._matlab:hsv", "category": "Cyclic"},
    "inferno": {
        "data": "cmap.data._matplotlib_new:Inferno",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "jet": {"data": "cmap.data._matlab:jet", "category": "Miscellaneous"},
    "magenta": {
        "data": "cmap.data._basic_colors:magenta",
        "category": "Sequential",
    },
    "magma": {
        "data": "cmap.data._matplotlib_new:Magma",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "nipy_spectral": {
        "data": "cmap.data._nipy:nipy_spectral",
        "category": "Miscellaneous",
    },
    "ocean": {
        "data": "cmap.data._gnuplot:ocean",
        "category": "Miscellaneous",
    },
    "pink": {"data": "cmap.data._matlab:pink", "tags": ["2"], "category": "Sequential"},
    "plasma": {
        "data": "cmap.data._matplotlib_new:Plasma",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "prism": {
        "data": "cmap.data._matlab:prism",
        "category": "Miscellaneous",
    },
    "rainbow": {
        "data": "cmap.data._gnuplot:rainbow",
        "category": "Miscellaneous",
    },
    "red": {
        "data": "cmap.data._basic_colors:red",
        "category": "Sequential",
    },
    "seismic": {
        "data": "cmap.data._matplotlib:seismic",
        "category": "Diverging",
    },
    "spring": {
        "data": "cmap.data._matlab:spring",
        "tags": ["2"],
        "category": "Sequential",
    },
    "summer": {
        "data": "cmap.data._matlab:summer",
        "tags": ["2"],
        "category": "Sequential",
    },
    "tab10": {
        "data": "cmap.data._tableau:Tableau10",
        "category": "Qualitative",
        "interpolation": False,
    },
    "tab10_colorblind": {
        "data": "cmap.data._tableau:ColorBlind10",
        "category": "Qualitative",
        "interpolation": False,
    },
    "tab10_light": {
        "data": "cmap.data._tableau:Tableau10_Light",
        "category": "Qualitative",
        "interpolation": False,
    },
    "tab10_medium": {
        "data": "cmap.data._tableau:Tableau10_Medium",
        "category": "Qualitative",
        "interpolation": False,
    },
    "tab20": {
        "data": "cmap.data._tableau:Tableau20",
        "category": "Qualitative",
        "interpolation": False,
    },
    "tab20b": {
        "data": "cmap.data._tableau:Tableau20b",
        "category": "Qualitative",
        "interpolation": False,
    },
    "tab20c": {
        "data": "cmap.data._tableau:Tableau20c",
        "category": "Qualitative",
        "interpolation": False,
    },
    "tab_traffic_light": {
        "data": "cmap.data._tableau:Traffic_Light",
        "category": "Qualitative",
        "interpolation": False,
    },
    "terrain": {
        "data": "cmap.data._igor:terrain",
        "category": "Miscellaneous",
    },
    "turbo": {
        "data": "cmap.data._turbo:Turbo",
        "category": "Miscellaneous",
    },
    "twilight": {
        "data": "cmap.data._matplotlib:Twilight",
        "category": "Cyclic",
    },
    "twilight_shifted": {
        "data": "cmap.data._matplotlib:Twilight_shifted",
        "category": "Cyclic",
    },
    "viridis": {
        "data": "cmap.data._matplotlib_new:Viridis",
        "tags": ["uniform"],
        "category": "Sequential",
    },
    "winter": {
        "data": "cmap.data._matlab:winter",
        "tags": ["2"],
        "category": "Sequential",
    },
    "yellow": {
        "data": "cmap.data._basic_colors:yellow",
        "category": "Sequential",
    },
    # vispy
    "vispy_light_blues": {
        "data": "cmap.data._vispy:light_blues",
        "category": "Sequential",
    },
    "vispy_single_hue": {
        "data": "cmap.data._vispy:single_hue",
        "category": "Sequential",
    },
    "vispy_orange": {  # problematic name
        "data": "cmap.data._vispy:orange",
        "category": "Sequential",
    },
    "vispy_GrBu": {  # name looks too much like colorbrewer
        "data": "cmap.data._vispy:GrBu",
        "category": "Diverging",
    },
    "vispy_GrBu_d": {  # name looks too much like colorbrewer
        "data": "cmap.data._vispy:GrBu_d",
        "category": "Diverging",
    },
    "vispy_PuGr": {  # name looks too much like colorbrewer
        "data": "cmap.data._vispy:PuGr",
        "category": "Diverging",
    },
    "vispy_RdBu": {
        "data": "cmap.data._vispy:RdBu",
        "category": "Diverging",
    },
    "vispy_diverging": {
        "data": "cmap.data._vispy:diverging",
        "category": "Diverging",
    },
    "vispy_husl": {
        "data": "cmap.data._vispy:husl",
        "category": "Sequential",
    },
    "vispy_hsl": {
        "data": "cmap.data._vispy:hsl",
        "category": "Sequential",
    },
    "vispy_fire": {
        "data": "cmap.data._vispy:fire",
        "category": "Sequential",
    },
    "vispy_ice": {
        "data": "cmap.data._vispy:ice",
        "category": "Sequential",
    },
    "vispy_RdYeBuCy": {
        "data": "cmap.data._vispy:RdYeBuCy",
        "category": "Diverging",
    },
    "glasbey": {
        "data": "cmap.data._glasbey:glasbey",
        "category": "Qualitative",
    },
    "imagej_fire": {
        "data": "cmap.data._imagej:Fire",
        "category": "Miscellaneous",
    },
    "imagej_ice": {
        "data": "cmap.data._imagej:Ice",
        "category": "Miscellaneous",
    },
    "Green_Fire_Blue": {
        "data": "cmap.data._imagej:Green_Fire_Blue",
        "category": "Miscellaneous",
    },
    "HiLo": {
        "data": "cmap.data._imagej:HiLo",
        "category": "Miscellaneous",
    },
    "algae": {
        "data": "cmap.data._cmocean.algae:algae",
        "category": "Sequential",
    },
    "amp": {
        "data": "cmap.data._cmocean.amp:amp",
        "category": "Sequential",
    },
    "balance": {
        "data": "cmap.data._cmocean.balance:balance",
        "category": "Diverging",
    },
    "balance_blue": {
        "data": "cmap.data._cmocean.balance:balance_blue",
        "category": "Sequential",
    },
    "balance_red": {
        "data": "cmap.data._cmocean.balance:balance_red",
        "category": "Sequential",
    },
    "delta": {
        "data": "cmap.data._cmocean.delta:delta",
        "category": "Diverging",
    },
    "delta_blue": {
        "data": "cmap.data._cmocean.delta:delta_blue",
        "category": "Sequential",
    },
    "delta_green": {
        "data": "cmap.data._cmocean.delta:delta_green",
        "category": "Sequential",
    },
    "curl": {
        "data": "cmap.data._cmocean.curl:curl",
        "category": "Diverging",
    },
    "curl_pink": {
        "data": "cmap.data._cmocean.curl:curl_pink",
        "category": "Sequential",
    },
    "curl_turquoise": {
        "data": "cmap.data._cmocean.curl:curl_turquoise",
        "category": "Sequential",
    },
    "diff": {
        "data": "cmap.data._cmocean.diff:diff",
        "category": "Diverging",
    },
    "tarn": {
        "data": "cmap.data._cmocean.tarn:tarn",
        "category": "Diverging",
    },
    "dense": {
        "data": "cmap.data._cmocean.dense:dense",
        "category": "Sequential",
    },
    "haline": {
        "data": "cmap.data._cmocean.haline:haline",
        "category": "Sequential",
    },
    "ice": {
        "data": "cmap.data._cmocean.ice:ice",
        "category": "Sequential",
    },
    "oxy": {
        "data": "cmap.data._cmocean.oxy:oxy",
        "category": "Sequential",
    },
    "phase": {
        "data": "cmap.data._cmocean.phase:phase",
        "category": "Cyclic",
    },
    "solar": {
        "data": "cmap.data._cmocean.solar:solar",
        "category": "Sequential",
    },
    "turbid": {
        "data": "cmap.data._cmocean.turbid:turbid",
        "category": "Sequential",
    },
    "thermal": {
        "data": "cmap.data._cmocean.thermal:thermal",
        "category": "Sequential",
    },
    "speed": {
        "data": "cmap.data._cmocean.speed:speed",
        "category": "Sequential",
    },
    "deep": {
        "data": "cmap.data._cmocean.deep:deep",
        "category": "Sequential",
    },
    "matter": {
        "data": "cmap.data._cmocean.matter:matter",
        "category": "Sequential",
    },
    "tempo": {
        "data": "cmap.data._cmocean.tempo:tempo",
        "category": "Sequential",
    },
    "rain": {
        "data": "cmap.data._cmocean.rain:rain",
        "category": "Sequential",
    },
    "topo": {
        "data": "cmap.data._cmocean.topo:topo",
        "category": "Miscellaneous",
    },
    "rocket": {
        "data": "cmap.data._seaborn:rocket",
        "category": "Sequential",
    },
    "mako": {
        "data": "cmap.data._seaborn:mako",
        "category": "Sequential",
    },
    "vlag": {
        "data": "cmap.data._seaborn:vlag",
        "category": "Diverging",
    },
    "icefire": {
        "data": "cmap.data._seaborn:icefire",
        "category": "Diverging",
    },
    "flare": {
        "data": "cmap.data._seaborn:flare",
        "category": "Sequential",
    },
    "crest": {
        "data": "cmap.data._seaborn:crest",
        "category": "Sequential",
    },
}


def _norm_name(name: str) -> str:
    return name.lower().replace(" ", "_")


_CATALOG_LOWER = {_norm_name(k): v for k, v in CATALOG.items()}


class Catalog:

    _loaded: dict[str, LoadedCatalogItem] = {}

    def __iter__(self) -> Iterator[str]:
        return iter(CATALOG)

    def items(self) -> Iterator[tuple[str, LoadedCatalogItem]]:
        for name in CATALOG:  # noqa: UP
            yield name, self[name]

    def __getitem__(self, name: str) -> LoadedCatalogItem:
        if name not in self._loaded:
            if (key := _norm_name(name)) not in _CATALOG_LOWER:
                # TODO: print a list of available colormaps or something
                if name != key:
                    raise ValueError(f"Colormap {name!r} (or {key!r}) not found.")
                raise ValueError(f"Colormap {name!r} not found.")

            self._loaded[name] = self._load(key)
            if key != name:
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
        item['source'] = item["data"]
        item["data"] = getattr(mod, attr)
        _item = cast("LoadedCatalogItem", item)
        _item["license"] = mod.__license__  # tests ensure this exists
        _item.setdefault("tags", [])
        return _item


catalog = Catalog()
