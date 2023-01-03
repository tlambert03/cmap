from typing import TYPE_CHECKING, Callable, cast

if TYPE_CHECKING:

    from numpy.typing import NDArray
    from typing_extensions import TypeAlias

    LutCallable: TypeAlias = Callable[[NDArray], NDArray]
    Data: TypeAlias = list[list[float]] | LutCallable
    CMRmap: Data
    cubehelix: Data
    Blues_3: Data
    Blues_4: Data
    Blues_5: Data
    Blues_6: Data
    Blues_7: Data
    Blues_8: Data
    Blues_9: Data
    Blues: Data
    BuGn_3: Data
    BuGn_4: Data
    BuGn_5: Data
    BuGn_6: Data
    BuGn_7: Data
    BuGn_8: Data
    BuGn_9: Data
    BuGn: Data
    BuPu_3: Data
    BuPu_4: Data
    BuPu_5: Data
    BuPu_6: Data
    BuPu_7: Data
    BuPu_8: Data
    BuPu_9: Data
    BuPu: Data
    GnBu_3: Data
    GnBu_4: Data
    GnBu_5: Data
    GnBu_6: Data
    GnBu_7: Data
    GnBu_8: Data
    GnBu_9: Data
    GnBu: Data
    Greens_3: Data
    Greens_4: Data
    Greens_5: Data
    Greens_6: Data
    Greens_7: Data
    Greens_8: Data
    Greens_9: Data
    Greens: Data
    Greys_3: Data
    Greys_4: Data
    Greys_5: Data
    Greys_6: Data
    Greys_7: Data
    Greys_8: Data
    Greys_9: Data
    Greys: Data
    Oranges_3: Data
    Oranges_4: Data
    Oranges_5: Data
    Oranges_6: Data
    Oranges_7: Data
    Oranges_8: Data
    Oranges_9: Data
    Oranges: Data
    OrRd_3: Data
    OrRd_4: Data
    OrRd_5: Data
    OrRd_6: Data
    OrRd_7: Data
    OrRd_8: Data
    OrRd_9: Data
    OrRd: Data
    PuBu_3: Data
    PuBu_4: Data
    PuBu_5: Data
    PuBu_6: Data
    PuBu_7: Data
    PuBu_8: Data
    PuBu_9: Data
    PuBu: Data
    PuBuGn_3: Data
    PuBuGn_4: Data
    PuBuGn_5: Data
    PuBuGn_6: Data
    PuBuGn_7: Data
    PuBuGn_8: Data
    PuBuGn_9: Data
    PuBuGn: Data
    PuRd_3: Data
    PuRd_4: Data
    PuRd_5: Data
    PuRd_6: Data
    PuRd_7: Data
    PuRd_8: Data
    PuRd_9: Data
    PuRd: Data
    Purples_3: Data
    Purples_4: Data
    Purples_5: Data
    Purples_6: Data
    Purples_7: Data
    Purples_8: Data
    Purples_9: Data
    Purples: Data
    RdPu_3: Data
    RdPu_4: Data
    RdPu_5: Data
    RdPu_6: Data
    RdPu_7: Data
    RdPu_8: Data
    RdPu_9: Data
    RdPu: Data
    Reds_3: Data
    Reds_4: Data
    Reds_5: Data
    Reds_6: Data
    Reds_7: Data
    Reds_8: Data
    Reds_9: Data
    Reds: Data
    YlGn_3: Data
    YlGn_4: Data
    YlGn_5: Data
    YlGn_6: Data
    YlGn_7: Data
    YlGn_8: Data
    YlGn_9: Data
    YlGn: Data
    YlGnBu_3: Data
    YlGnBu_4: Data
    YlGnBu_5: Data
    YlGnBu_6: Data
    YlGnBu_7: Data
    YlGnBu_8: Data
    YlGnBu_9: Data
    YlGnBu: Data
    YlOrBr_3: Data
    YlOrBr_4: Data
    YlOrBr_5: Data
    YlOrBr_6: Data
    YlOrBr_7: Data
    YlOrBr_8: Data
    YlOrBr_9: Data
    YlOrBr: Data
    YlOrRd_3: Data
    YlOrRd_4: Data
    YlOrRd_5: Data
    YlOrRd_6: Data
    YlOrRd_7: Data
    YlOrRd_8: Data
    YlOrRd_9: Data
    YlOrRd: Data
    BrBG_3: Data
    BrBG_4: Data
    BrBG_5: Data
    BrBG_6: Data
    BrBG_7: Data
    BrBG_8: Data
    BrBG_9: Data
    BrBG_10: Data
    BrBG_11: Data
    BrBG: Data
    PiYG_3: Data
    PiYG_4: Data
    PiYG_5: Data
    PiYG_6: Data
    PiYG_7: Data
    PiYG_8: Data
    PiYG_9: Data
    PiYG_10: Data
    PiYG_11: Data
    PiYG: Data
    PRGn_3: Data
    PRGn_4: Data
    PRGn_5: Data
    PRGn_6: Data
    PRGn_7: Data
    PRGn_8: Data
    PRGn_9: Data
    PRGn_10: Data
    PRGn_11: Data
    PRGn: Data
    PuOr_3: Data
    PuOr_4: Data
    PuOr_5: Data
    PuOr_6: Data
    PuOr_7: Data
    PuOr_8: Data
    PuOr_9: Data
    PuOr_10: Data
    PuOr_11: Data
    PuOr: Data
    RdBu_3: Data
    RdBu_4: Data
    RdBu_5: Data
    RdBu_6: Data
    RdBu_7: Data
    RdBu_8: Data
    RdBu_9: Data
    RdBu_10: Data
    RdBu_11: Data
    RdBu: Data
    RdGy_3: Data
    RdGy_4: Data
    RdGy_5: Data
    RdGy_6: Data
    RdGy_7: Data
    RdGy_8: Data
    RdGy_9: Data
    RdGy_10: Data
    RdGy_11: Data
    RdGy: Data
    RdYlBu_3: Data
    RdYlBu_4: Data
    RdYlBu_5: Data
    RdYlBu_6: Data
    RdYlBu_7: Data
    RdYlBu_8: Data
    RdYlBu_9: Data
    RdYlBu_10: Data
    RdYlBu_11: Data
    RdYlBu: Data
    RdYlGn_3: Data
    RdYlGn_4: Data
    RdYlGn_5: Data
    RdYlGn_6: Data
    RdYlGn_7: Data
    RdYlGn_8: Data
    RdYlGn_9: Data
    RdYlGn_10: Data
    RdYlGn_11: Data
    RdYlGn: Data
    Spectral_3: Data
    Spectral_4: Data
    Spectral_5: Data
    Spectral_6: Data
    Spectral_7: Data
    Spectral_8: Data
    Spectral_9: Data
    Spectral_10: Data
    Spectral_11: Data
    Spectral: Data
    Accent_3: Data
    Accent_4: Data
    Accent_5: Data
    Accent_6: Data
    Accent_7: Data
    Accent_8: Data
    Accent: Data
    Dark2_3: Data
    Dark2_4: Data
    Dark2_5: Data
    Dark2_6: Data
    Dark2_7: Data
    Dark2_8: Data
    Dark2: Data
    Paired_3: Data
    Paired_4: Data
    Paired_5: Data
    Paired_6: Data
    Paired_7: Data
    Paired_8: Data
    Paired_9: Data
    Paired_10: Data
    Paired_11: Data
    Paired_12: Data
    Paired: Data
    Pastel1_3: Data
    Pastel1_4: Data
    Pastel1_5: Data
    Pastel1_6: Data
    Pastel1_7: Data
    Pastel1_8: Data
    Pastel1_9: Data
    Pastel1: Data
    Pastel2_3: Data
    Pastel2_4: Data
    Pastel2_5: Data
    Pastel2_6: Data
    Pastel2_7: Data
    Pastel2_8: Data
    Pastel2: Data
    Set1_3: Data
    Set1_4: Data
    Set1_5: Data
    Set1_6: Data
    Set1_7: Data
    Set1_8: Data
    Set1_9: Data
    Set1: Data
    Set2_3: Data
    Set2_4: Data
    Set2_5: Data
    Set2_6: Data
    Set2_7: Data
    Set2_8: Data
    Set2: Data
    Set3_3: Data
    Set3_4: Data
    Set3_5: Data
    Set3_6: Data
    Set3_7: Data
    Set3_8: Data
    Set3_9: Data
    Set3_10: Data
    Set3_11: Data
    Set3_12: Data
    Set3: Data
    Wistia: Data
    gnuplot: Data
    ocean: Data
    hot: Data
    gnuplot2: Data
    rainbow: Data
    afmhot: Data
    hsv: Data
    gist_gray: Data
    gist_earth: Data
    gist_ncar: Data
    gist_heat: Data
    gist_rainbow: Data
    gist_stern: Data
    gist_yarg: Data
    binary: Data
    magma: Data
    inferno: Data
    plasma: Data
    viridis: Data
    cividis: Data
    twilight: Data
    twilight_shifted: Data
    turbo: Data
    seismic: Data
    bwr: Data
    brg: Data
    terrain: Data
    nipy_spectral: Data
    coolwarm: Data
    flag: Data
    gray: Data
    autumn: Data
    bone: Data
    cool: Data
    copper: Data
    spring: Data
    summer: Data
    winter: Data
    pink: Data
    prism: Data
    jet: Data
    tab10: Data
    tab10_light: Data
    tab10_medium: Data
    tab10_colorblind: Data
    tab20: Data
    tab20b: Data
    tab20c: Data
    tab_traffic_light: Data


_DATA = {
    "CMRmap": "_CMRmap:CMRmap",
    "cubehelix": "_cubehelix:cubehelix",
    "Blues_3": "_colorbrewer:Blues_3",
    "Blues_4": "_colorbrewer:Blues_4",
    "Blues_5": "_colorbrewer:Blues_5",
    "Blues_6": "_colorbrewer:Blues_6",
    "Blues_7": "_colorbrewer:Blues_7",
    "Blues_8": "_colorbrewer:Blues_8",
    "Blues_9": "_colorbrewer:Blues_9",
    "Blues": "_colorbrewer:Blues_9",  # alias
    "BuGn_3": "_colorbrewer:BuGn_3",
    "BuGn_4": "_colorbrewer:BuGn_4",
    "BuGn_5": "_colorbrewer:BuGn_5",
    "BuGn_6": "_colorbrewer:BuGn_6",
    "BuGn_7": "_colorbrewer:BuGn_7",
    "BuGn_8": "_colorbrewer:BuGn_8",
    "BuGn_9": "_colorbrewer:BuGn_9",
    "BuGn": "_colorbrewer:BuGn_9",  # alias
    "BuPu_3": "_colorbrewer:BuPu_3",
    "BuPu_4": "_colorbrewer:BuPu_4",
    "BuPu_5": "_colorbrewer:BuPu_5",
    "BuPu_6": "_colorbrewer:BuPu_6",
    "BuPu_7": "_colorbrewer:BuPu_7",
    "BuPu_8": "_colorbrewer:BuPu_8",
    "BuPu_9": "_colorbrewer:BuPu_9",
    "BuPu": "_colorbrewer:BuPu_9",  # alias
    "GnBu_3": "_colorbrewer:GnBu_3",
    "GnBu_4": "_colorbrewer:GnBu_4",
    "GnBu_5": "_colorbrewer:GnBu_5",
    "GnBu_6": "_colorbrewer:GnBu_6",
    "GnBu_7": "_colorbrewer:GnBu_7",
    "GnBu_8": "_colorbrewer:GnBu_8",
    "GnBu_9": "_colorbrewer:GnBu_9",
    "GnBu": "_colorbrewer:GnBu_9",  # alias
    "Greens_3": "_colorbrewer:Greens_3",
    "Greens_4": "_colorbrewer:Greens_4",
    "Greens_5": "_colorbrewer:Greens_5",
    "Greens_6": "_colorbrewer:Greens_6",
    "Greens_7": "_colorbrewer:Greens_7",
    "Greens_8": "_colorbrewer:Greens_8",
    "Greens_9": "_colorbrewer:Greens_9",
    "Greens": "_colorbrewer:Greens_9",  # alias
    "Greys_3": "_colorbrewer:Greys_3",
    "Greys_4": "_colorbrewer:Greys_4",
    "Greys_5": "_colorbrewer:Greys_5",
    "Greys_6": "_colorbrewer:Greys_6",
    "Greys_7": "_colorbrewer:Greys_7",
    "Greys_8": "_colorbrewer:Greys_8",
    "Greys_9": "_colorbrewer:Greys_9",
    "Greys": "_colorbrewer:Greys_9",  # alias
    "Oranges_3": "_colorbrewer:Oranges_3",
    "Oranges_4": "_colorbrewer:Oranges_4",
    "Oranges_5": "_colorbrewer:Oranges_5",
    "Oranges_6": "_colorbrewer:Oranges_6",
    "Oranges_7": "_colorbrewer:Oranges_7",
    "Oranges_8": "_colorbrewer:Oranges_8",
    "Oranges_9": "_colorbrewer:Oranges_9",
    "Oranges": "_colorbrewer:Oranges_9",  # alias
    "OrRd_3": "_colorbrewer:OrRd_3",
    "OrRd_4": "_colorbrewer:OrRd_4",
    "OrRd_5": "_colorbrewer:OrRd_5",
    "OrRd_6": "_colorbrewer:OrRd_6",
    "OrRd_7": "_colorbrewer:OrRd_7",
    "OrRd_8": "_colorbrewer:OrRd_8",
    "OrRd_9": "_colorbrewer:OrRd_9",
    "OrRd": "_colorbrewer:OrRd_9",  # alias
    "PuBu_3": "_colorbrewer:PuBu_3",
    "PuBu_4": "_colorbrewer:PuBu_4",
    "PuBu_5": "_colorbrewer:PuBu_5",
    "PuBu_6": "_colorbrewer:PuBu_6",
    "PuBu_7": "_colorbrewer:PuBu_7",
    "PuBu_8": "_colorbrewer:PuBu_8",
    "PuBu_9": "_colorbrewer:PuBu_9",
    "PuBu": "_colorbrewer:PuBu_9",  # alias
    "PuBuGn_3": "_colorbrewer:PuBuGn_3",
    "PuBuGn_4": "_colorbrewer:PuBuGn_4",
    "PuBuGn_5": "_colorbrewer:PuBuGn_5",
    "PuBuGn_6": "_colorbrewer:PuBuGn_6",
    "PuBuGn_7": "_colorbrewer:PuBuGn_7",
    "PuBuGn_8": "_colorbrewer:PuBuGn_8",
    "PuBuGn_9": "_colorbrewer:PuBuGn_9",
    "PuBuGn": "_colorbrewer:PuBuGn_9",  # alias
    "PuRd_3": "_colorbrewer:PuRd_3",
    "PuRd_4": "_colorbrewer:PuRd_4",
    "PuRd_5": "_colorbrewer:PuRd_5",
    "PuRd_6": "_colorbrewer:PuRd_6",
    "PuRd_7": "_colorbrewer:PuRd_7",
    "PuRd_8": "_colorbrewer:PuRd_8",
    "PuRd_9": "_colorbrewer:PuRd_9",
    "PuRd": "_colorbrewer:PuRd_9",  # alias
    "Purples_3": "_colorbrewer:Purples_3",
    "Purples_4": "_colorbrewer:Purples_4",
    "Purples_5": "_colorbrewer:Purples_5",
    "Purples_6": "_colorbrewer:Purples_6",
    "Purples_7": "_colorbrewer:Purples_7",
    "Purples_8": "_colorbrewer:Purples_8",
    "Purples_9": "_colorbrewer:Purples_9",
    "Purples": "_colorbrewer:Purples_9",  # alias
    "RdPu_3": "_colorbrewer:RdPu_3",
    "RdPu_4": "_colorbrewer:RdPu_4",
    "RdPu_5": "_colorbrewer:RdPu_5",
    "RdPu_6": "_colorbrewer:RdPu_6",
    "RdPu_7": "_colorbrewer:RdPu_7",
    "RdPu_8": "_colorbrewer:RdPu_8",
    "RdPu_9": "_colorbrewer:RdPu_9",
    "RdPu": "_colorbrewer:RdPu_9",  # alias
    "Reds_3": "_colorbrewer:Reds_3",
    "Reds_4": "_colorbrewer:Reds_4",
    "Reds_5": "_colorbrewer:Reds_5",
    "Reds_6": "_colorbrewer:Reds_6",
    "Reds_7": "_colorbrewer:Reds_7",
    "Reds_8": "_colorbrewer:Reds_8",
    "Reds_9": "_colorbrewer:Reds_9",
    "Reds": "_colorbrewer:Reds_9",  # alias
    "YlGn_3": "_colorbrewer:YlGn_3",
    "YlGn_4": "_colorbrewer:YlGn_4",
    "YlGn_5": "_colorbrewer:YlGn_5",
    "YlGn_6": "_colorbrewer:YlGn_6",
    "YlGn_7": "_colorbrewer:YlGn_7",
    "YlGn_8": "_colorbrewer:YlGn_8",
    "YlGn_9": "_colorbrewer:YlGn_9",
    "YlGn": "_colorbrewer:YlGn_9",  # alias
    "YlGnBu_3": "_colorbrewer:YlGnBu_3",
    "YlGnBu_4": "_colorbrewer:YlGnBu_4",
    "YlGnBu_5": "_colorbrewer:YlGnBu_5",
    "YlGnBu_6": "_colorbrewer:YlGnBu_6",
    "YlGnBu_7": "_colorbrewer:YlGnBu_7",
    "YlGnBu_8": "_colorbrewer:YlGnBu_8",
    "YlGnBu_9": "_colorbrewer:YlGnBu_9",
    "YlGnBu": "_colorbrewer:YlGnBu_9",  # alias
    "YlOrBr_3": "_colorbrewer:YlOrBr_3",
    "YlOrBr_4": "_colorbrewer:YlOrBr_4",
    "YlOrBr_5": "_colorbrewer:YlOrBr_5",
    "YlOrBr_6": "_colorbrewer:YlOrBr_6",
    "YlOrBr_7": "_colorbrewer:YlOrBr_7",
    "YlOrBr_8": "_colorbrewer:YlOrBr_8",
    "YlOrBr_9": "_colorbrewer:YlOrBr_9",
    "YlOrBr": "_colorbrewer:YlOrBr_9",  # alias
    "YlOrRd_3": "_colorbrewer:YlOrRd_3",
    "YlOrRd_4": "_colorbrewer:YlOrRd_4",
    "YlOrRd_5": "_colorbrewer:YlOrRd_5",
    "YlOrRd_6": "_colorbrewer:YlOrRd_6",
    "YlOrRd_7": "_colorbrewer:YlOrRd_7",
    "YlOrRd_8": "_colorbrewer:YlOrRd_8",
    "YlOrRd_9": "_colorbrewer:YlOrRd_9",
    "YlOrRd": "_colorbrewer:YlOrRd_9",  # alias
    "BrBG_3": "_colorbrewer:BrBG_3",
    "BrBG_4": "_colorbrewer:BrBG_4",
    "BrBG_5": "_colorbrewer:BrBG_5",
    "BrBG_6": "_colorbrewer:BrBG_6",
    "BrBG_7": "_colorbrewer:BrBG_7",
    "BrBG_8": "_colorbrewer:BrBG_8",
    "BrBG_9": "_colorbrewer:BrBG_9",
    "BrBG_10": "_colorbrewer:BrBG_10",
    "BrBG_11": "_colorbrewer:BrBG_11",
    "BrBG": "_colorbrewer:BrBG_11",  # alias
    "PiYG_3": "_colorbrewer:PiYG_3",
    "PiYG_4": "_colorbrewer:PiYG_4",
    "PiYG_5": "_colorbrewer:PiYG_5",
    "PiYG_6": "_colorbrewer:PiYG_6",
    "PiYG_7": "_colorbrewer:PiYG_7",
    "PiYG_8": "_colorbrewer:PiYG_8",
    "PiYG_9": "_colorbrewer:PiYG_9",
    "PiYG_10": "_colorbrewer:PiYG_10",
    "PiYG_11": "_colorbrewer:PiYG_11",
    "PiYG": "_colorbrewer:PiYG_11",  # alias
    "PRGn_3": "_colorbrewer:PRGn_3",
    "PRGn_4": "_colorbrewer:PRGn_4",
    "PRGn_5": "_colorbrewer:PRGn_5",
    "PRGn_6": "_colorbrewer:PRGn_6",
    "PRGn_7": "_colorbrewer:PRGn_7",
    "PRGn_8": "_colorbrewer:PRGn_8",
    "PRGn_9": "_colorbrewer:PRGn_9",
    "PRGn_10": "_colorbrewer:PRGn_10",
    "PRGn_11": "_colorbrewer:PRGn_11",
    "PRGn": "_colorbrewer:PRGn_11",  # alias
    "PuOr_3": "_colorbrewer:PuOr_3",
    "PuOr_4": "_colorbrewer:PuOr_4",
    "PuOr_5": "_colorbrewer:PuOr_5",
    "PuOr_6": "_colorbrewer:PuOr_6",
    "PuOr_7": "_colorbrewer:PuOr_7",
    "PuOr_8": "_colorbrewer:PuOr_8",
    "PuOr_9": "_colorbrewer:PuOr_9",
    "PuOr_10": "_colorbrewer:PuOr_10",
    "PuOr_11": "_colorbrewer:PuOr_11",
    "PuOr": "_colorbrewer:PuOr_11",  # alias
    "RdBu_3": "_colorbrewer:RdBu_3",
    "RdBu_4": "_colorbrewer:RdBu_4",
    "RdBu_5": "_colorbrewer:RdBu_5",
    "RdBu_6": "_colorbrewer:RdBu_6",
    "RdBu_7": "_colorbrewer:RdBu_7",
    "RdBu_8": "_colorbrewer:RdBu_8",
    "RdBu_9": "_colorbrewer:RdBu_9",
    "RdBu_10": "_colorbrewer:RdBu_10",
    "RdBu_11": "_colorbrewer:RdBu_11",
    "RdBu": "_colorbrewer:RdBu_11",  # alias
    "RdGy_3": "_colorbrewer:RdGy_3",
    "RdGy_4": "_colorbrewer:RdGy_4",
    "RdGy_5": "_colorbrewer:RdGy_5",
    "RdGy_6": "_colorbrewer:RdGy_6",
    "RdGy_7": "_colorbrewer:RdGy_7",
    "RdGy_8": "_colorbrewer:RdGy_8",
    "RdGy_9": "_colorbrewer:RdGy_9",
    "RdGy_10": "_colorbrewer:RdGy_10",
    "RdGy_11": "_colorbrewer:RdGy_11",
    "RdGy": "_colorbrewer:RdGy_11",  # alias
    "RdYlBu_3": "_colorbrewer:RdYlBu_3",
    "RdYlBu_4": "_colorbrewer:RdYlBu_4",
    "RdYlBu_5": "_colorbrewer:RdYlBu_5",
    "RdYlBu_6": "_colorbrewer:RdYlBu_6",
    "RdYlBu_7": "_colorbrewer:RdYlBu_7",
    "RdYlBu_8": "_colorbrewer:RdYlBu_8",
    "RdYlBu_9": "_colorbrewer:RdYlBu_9",
    "RdYlBu_10": "_colorbrewer:RdYlBu_10",
    "RdYlBu_11": "_colorbrewer:RdYlBu_11",
    "RdYlBu": "_colorbrewer:RdYlBu_11",  # alias
    "RdYlGn_3": "_colorbrewer:RdYlGn_3",
    "RdYlGn_4": "_colorbrewer:RdYlGn_4",
    "RdYlGn_5": "_colorbrewer:RdYlGn_5",
    "RdYlGn_6": "_colorbrewer:RdYlGn_6",
    "RdYlGn_7": "_colorbrewer:RdYlGn_7",
    "RdYlGn_8": "_colorbrewer:RdYlGn_8",
    "RdYlGn_9": "_colorbrewer:RdYlGn_9",
    "RdYlGn_10": "_colorbrewer:RdYlGn_10",
    "RdYlGn_11": "_colorbrewer:RdYlGn_11",
    "RdYlGn": "_colorbrewer:RdYlGn_11",  # alias
    "Spectral_3": "_colorbrewer:Spectral_3",
    "Spectral_4": "_colorbrewer:Spectral_4",
    "Spectral_5": "_colorbrewer:Spectral_5",
    "Spectral_6": "_colorbrewer:Spectral_6",
    "Spectral_7": "_colorbrewer:Spectral_7",
    "Spectral_8": "_colorbrewer:Spectral_8",
    "Spectral_9": "_colorbrewer:Spectral_9",
    "Spectral_10": "_colorbrewer:Spectral_10",
    "Spectral_11": "_colorbrewer:Spectral_11",
    "Spectral": "_colorbrewer:Spectral_11",  # alias
    "Accent_3": "_colorbrewer:Accent_3",
    "Accent_4": "_colorbrewer:Accent_4",
    "Accent_5": "_colorbrewer:Accent_5",
    "Accent_6": "_colorbrewer:Accent_6",
    "Accent_7": "_colorbrewer:Accent_7",
    "Accent_8": "_colorbrewer:Accent_8",
    "Accent": "_colorbrewer:Accent_8",  # alias
    "Dark2_3": "_colorbrewer:Dark2_3",
    "Dark2_4": "_colorbrewer:Dark2_4",
    "Dark2_5": "_colorbrewer:Dark2_5",
    "Dark2_6": "_colorbrewer:Dark2_6",
    "Dark2_7": "_colorbrewer:Dark2_7",
    "Dark2_8": "_colorbrewer:Dark2_8",
    "Dark2": "_colorbrewer:Dark2_8",  # alias
    "Paired_3": "_colorbrewer:Paired_3",
    "Paired_4": "_colorbrewer:Paired_4",
    "Paired_5": "_colorbrewer:Paired_5",
    "Paired_6": "_colorbrewer:Paired_6",
    "Paired_7": "_colorbrewer:Paired_7",
    "Paired_8": "_colorbrewer:Paired_8",
    "Paired_9": "_colorbrewer:Paired_9",
    "Paired_10": "_colorbrewer:Paired_10",
    "Paired_11": "_colorbrewer:Paired_11",
    "Paired_12": "_colorbrewer:Paired_12",
    "Paired": "_colorbrewer:Paired_12",  # alias
    "Pastel1_3": "_colorbrewer:Pastel1_3",
    "Pastel1_4": "_colorbrewer:Pastel1_4",
    "Pastel1_5": "_colorbrewer:Pastel1_5",
    "Pastel1_6": "_colorbrewer:Pastel1_6",
    "Pastel1_7": "_colorbrewer:Pastel1_7",
    "Pastel1_8": "_colorbrewer:Pastel1_8",
    "Pastel1_9": "_colorbrewer:Pastel1_9",
    "Pastel1": "_colorbrewer:Pastel1_9",  # alias
    "Pastel2_3": "_colorbrewer:Pastel2_3",
    "Pastel2_4": "_colorbrewer:Pastel2_4",
    "Pastel2_5": "_colorbrewer:Pastel2_5",
    "Pastel2_6": "_colorbrewer:Pastel2_6",
    "Pastel2_7": "_colorbrewer:Pastel2_7",
    "Pastel2_8": "_colorbrewer:Pastel2_8",
    "Pastel2": "_colorbrewer:Pastel2_8",  # alias
    "Set1_3": "_colorbrewer:Set1_3",
    "Set1_4": "_colorbrewer:Set1_4",
    "Set1_5": "_colorbrewer:Set1_5",
    "Set1_6": "_colorbrewer:Set1_6",
    "Set1_7": "_colorbrewer:Set1_7",
    "Set1_8": "_colorbrewer:Set1_8",
    "Set1_9": "_colorbrewer:Set1_9",
    "Set1": "_colorbrewer:Set1_9",  # alias
    "Set2_3": "_colorbrewer:Set2_3",
    "Set2_4": "_colorbrewer:Set2_4",
    "Set2_5": "_colorbrewer:Set2_5",
    "Set2_6": "_colorbrewer:Set2_6",
    "Set2_7": "_colorbrewer:Set2_7",
    "Set2_8": "_colorbrewer:Set2_8",
    "Set2": "_colorbrewer:Set2_8",  # alias
    "Set3_3": "_colorbrewer:Set3_3",
    "Set3_4": "_colorbrewer:Set3_4",
    "Set3_5": "_colorbrewer:Set3_5",
    "Set3_6": "_colorbrewer:Set3_6",
    "Set3_7": "_colorbrewer:Set3_7",
    "Set3_8": "_colorbrewer:Set3_8",
    "Set3_9": "_colorbrewer:Set3_9",
    "Set3_10": "_colorbrewer:Set3_10",
    "Set3_11": "_colorbrewer:Set3_11",
    "Set3_12": "_colorbrewer:Set3_12",
    "Set3": "_colorbrewer:Set3_12",  # alias
    "Wistia": "_wistia:Wistia",
    "gnuplot": "_gnuplot:gnuplot",
    # "grv" : "_gnuplot:grv",
    "ocean": "_gnuplot:ocean",
    "hot": "_gnuplot:hot",
    "gnuplot2": "_gnuplot:gnuplot2",
    "rainbow": "_gnuplot:rainbow",
    "afmhot": "_gnuplot:afmhot",
    "hsv": "_gnuplot:hsv",
    "gist_gray": "_gnuplot:gist_gray",
    "gist_earth": "_yorik:earth",
    "gist_ncar": "_yorik:ncar",
    "gist_heat": "_yorik:heat",
    "gist_rainbow": "_yorik:rainbow",
    "gist_stern": "_yorik:stern",
    "gist_yarg": "_yorik:yarg",
    "binary": "_yorik:yarg",  # seems to be an alias
    "magma": "_matplotlib:Magma",
    "inferno": "_matplotlib:Inferno",
    "plasma": "_matplotlib:Plasma",
    "viridis": "_matplotlib:Viridis",
    "cividis": "_matplotlib:Cividis",
    "twilight": "_matplotlib:Twilight",
    "twilight_shifted": "_matplotlib:Twilight_shifted",
    "turbo": "_matplotlib:Turbo",
    "seismic": "_matplotlib:seismic",
    "bwr": "_matplotlib:bwr",
    "brg": "_matplotlib:brg",
    "terrain": "_igor:terrain",
    "nipy_spectral": "_nipy:nipy_spectral",
    "coolwarm": "_moreland:CoolWarm",
    "flag": "_matlab:flag",
    "gray": "_matlab:gray",
    "autumn": "_matlab:autumn",
    "bone": "_matlab:bone",
    "cool": "_matlab:cool",
    "copper": "_matlab:copper",
    "spring": "_matlab:spring",
    "summer": "_matlab:summer",
    "winter": "_matlab:winter",
    "pink": "_matlab:pink",
    "prism": "_matlab:prism",
    "jet": "_matlab:jet",
    "tab10": "_tableau:Tableau10",
    "tab10_light": "_tableau:Tableau10_Light",
    "tab10_medium": "_tableau:Tableau10_Medium",
    "tab10_colorblind": "_tableau:ColorBlind10",
    "tab20": "_tableau:Tableau20",
    "tab20b": "_tableau:Tableau20b",
    "tab20c": "_tableau:Tableau20c",
    "tab_traffic_light": "_tableau:Traffic_Light",
}


def __dir__() -> list[str]:
    return list(_DATA)


_DATA_LOWER = {k.lower(): v for k, v in _DATA.items()}


def __getattr__(name: str) -> "Data":
    if (lower := name.lower()) in _DATA_LOWER:
        from importlib import import_module

        module_name, data_name = _DATA_LOWER[lower].split(":")
        module = import_module(f".{module_name}", __package__)
        return cast("Data", getattr(module, data_name))

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
