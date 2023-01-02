"""Color schemes from gnuplot.

https://gnuplot.sourceforge.net

#### GNUPLOT RGB FORMULAE ########################################

# List of palette functions in Gnuplot (show palette rgbformulae).
# Note that "180x" corresponds to pi*x etc. since built-in trig
# functions use radians.
#   00: 0              01: 0.5            02: 1
#   03: x              04: x^2            05: x^3
#   06: x^4            07: sqrt(x)        08: sqrt(sqrt(x))
#   09: sin(90x)       10: cos(90x)       11: |x-0.5|
#   12: (2x-1)^2       13: sin(180x)      14: |cos(180x)|
#   15: sin(360x)      16: cos(360x)      17: |sin(360x)|
#   18: |cos(360x)|    19: |sin(720x)|    20: |cos(720x)|
#   21: 3x             22: 3x-1           23: 3x-2
#   24: |3x-1|         25: |3x-2|         26: (3x-1)/2
#   27: (3x-2)/2       28: |(3x-1)/2|     29: |(3x-2)/2|
#   30: x/0.32-0.78125 31: 2*x-0.84       32: 4x;1;-2x+1.84;x/0.08-11.5
#   33: |2*x - 0.5|    34: 2*x            35: 2*x - 0.5
#   36: 2*x - 1
"""
from functools import partial
from typing import TYPE_CHECKING, Sequence, cast

import numpy as np

if TYPE_CHECKING:
    from typing import Callable

    from numpy.typing import NDArray
    from typing_extensions import TypeAlias

    ArrayMapper: TypeAlias = Callable[[NDArray], NDArray]


# fmt: off
def _g0(x): return np.zeros_like(x)
def _g1(x): return 0.5 * np.ones_like(x)
def _g2(x): return np.ones_like(x)
def _g3(x): return x
def _g4(x): return x ** 2
def _g5(x): return x ** 3
def _g6(x): return x ** 4
def _g7(x): return np.sqrt(x)
def _g8(x): return np.sqrt(np.sqrt(x))
def _g9(x): return np.sin(x * np.pi / 2)
def _g10(x): return np.cos(x * np.pi / 2)
def _g11(x): return np.abs(x - 0.5)
def _g12(x): return (2 * x - 1) ** 2
def _g13(x): return np.sin(x * np.pi)
def _g14(x): return np.abs(np.cos(x * np.pi))
def _g15(x): return np.sin(x * 2 * np.pi)
def _g16(x): return np.cos(x * 2 * np.pi)
def _g17(x): return np.abs(np.sin(x * 2 * np.pi))
def _g18(x): return np.abs(np.cos(x * 2 * np.pi))
def _g19(x): return np.abs(np.sin(x * 4 * np.pi))
def _g20(x): return np.abs(np.cos(x * 4 * np.pi))
def _g21(x): return 3 * x
def _g22(x): return 3 * x - 1
def _g23(x): return 3 * x - 2
def _g24(x): return np.abs(3 * x - 1)
def _g25(x): return np.abs(3 * x - 2)
def _g26(x): return (3 * x - 1) / 2
def _g27(x): return (3 * x - 2) / 2
def _g28(x): return np.abs((3 * x - 1) / 2)
def _g29(x): return np.abs((3 * x - 2) / 2)
def _g30(x): return x / 0.32 - 0.78125
def _g31(x): return 2 * x - 0.84
def _g32(x):
    ret = np.zeros(len(x))
    m = (x < 0.25)
    ret[m] = 4 * x[m]
    m = (x >= 0.25) & (x < 0.92)
    ret[m] = -2 * x[m] + 1.84
    m = (x >= 0.92)
    ret[m] = x[m] / 0.08 - 11.5
    return ret
def _g33(x): return np.abs(2 * x - 0.5)
def _g34(x): return 2 * x
def _g35(x): return 2 * x - 0.5
def _g36(x): return 2 * x - 1
# fmt: on


def _combine_gnufunc(mappers: Sequence["ArrayMapper"], ary: "NDArray") -> "NDArray":
    """Helper function for combining multiple gnuplot formulae."""
    return np.stack([_g(np.asarray(ary)) for _g in mappers], axis=-1)


def _combine_gnufunc_hsv(mappers: Sequence["ArrayMapper"], ary: "NDArray") -> "NDArray":
    """Helper function for combining multiple gnuplot formulae in hsv space."""
    hsv_data = np.stack([_g(np.asarray(ary)) for _g in mappers], axis=-1)
    return hsv_to_rgb(hsv_data)


def hsv_to_rgb(hsv: "NDArray") -> "NDArray":
    """Convert hsv values to rgb.

    Parameters
    ----------
    hsv : (N, 3) ndarray
       All values assumed to be in range [0, 1]

    Returns
    -------
    (N, 3) ndarray
       Colors converted to RGB values in range [0, 1]
    """
    in_shape = hsv.shape
    hsv = np.array(
        hsv,
        copy=False,
        dtype=np.promote_types(hsv.dtype, np.float32),  # Don't work on ints.
        ndmin=2,  # In case input was 1D.
    )

    h = hsv[..., 0]
    s = hsv[..., 1]
    v = hsv[..., 2]

    r = np.empty_like(h)
    g = np.empty_like(h)
    b = np.empty_like(h)

    i = (h * 6.0).astype(int)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))

    idx = i % 6 == 0
    r[idx] = v[idx]
    g[idx] = t[idx]
    b[idx] = p[idx]

    idx = i == 1
    r[idx] = q[idx]
    g[idx] = v[idx]
    b[idx] = p[idx]

    idx = i == 2
    r[idx] = p[idx]
    g[idx] = v[idx]
    b[idx] = t[idx]

    idx = i == 3
    r[idx] = p[idx]
    g[idx] = q[idx]
    b[idx] = v[idx]

    idx = i == 4
    r[idx] = t[idx]
    g[idx] = p[idx]
    b[idx] = v[idx]

    idx = i == 5
    r[idx] = v[idx]
    g[idx] = p[idx]
    b[idx] = q[idx]

    idx = s == 0
    r[idx] = v[idx]
    g[idx] = v[idx]
    b[idx] = v[idx]

    rgb = np.stack([r, g, b], axis=-1)

    return cast("NDArray", rgb.reshape(in_shape))


# https://web.mit.edu/gnuplot_v4.2/doc/htmldocs/node216.html
# Some nice schemes in RGB color space

#   7,5,15   ... traditional pm3d (black-blue-red-yellow)
gnuplot = partial(_combine_gnufunc, (_g7, _g5, _g15))
#   3,11,6   ... green-red-violet
grv = partial(_combine_gnufunc, (_g3, _g11, _g6))
#   23,28,3  ... ocean (green-blue-white); try also all other permutations
ocean = partial(_combine_gnufunc, (_g23, _g28, _g3))
#   21,22,23 ... hot (black-red-yellow-white)
hot = partial(_combine_gnufunc, (_g21, _g22, _g23))
#   30,31,32 ... color printable on gray (black-blue-violet-yellow-white)
gnuplot2 = partial(_combine_gnufunc, (_g30, _g31, _g32))
#   33,13,10 ... rainbow (blue-green-yellow-red)
rainbow = partial(_combine_gnufunc, (_g33, _g13, _g10))
#   34,35,36 ... AFM hot (black-red-yellow-white)
afmhot = partial(_combine_gnufunc, (_g34, _g35, _g36))

gist_gray = partial(_combine_gnufunc, (_g3, _g3, _g3))

# A full color palette in HSV color space
# 3,2,2    ... red-yellow-green-cyan-blue-magenta-red
hsv = partial(_combine_gnufunc_hsv, (_g3, _g2, _g2))
