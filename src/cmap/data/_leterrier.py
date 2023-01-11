"""Colormaps from Christophe Leterrier.

https://github.com/cleterrier/ChrisLUTs

All the LUTs in this module have been devised by Christophe Leterrier
and are available under an MIT license.

MIT License

Copyright (c) 2020 Christophe Leterrier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
__license__ = "MIT"
__source__ = "https://github.com/cleterrier/ChrisLUTs"

# Note: ChrisLUTs supplies these as a full 256x3 matrix,
# but they're all linear ramps, so we let the colormap do the interpolation


BOP_Blue = [[0, 0, 0], [32, 173, 248]]
BOP_Orange = [[0, 0, 0], [237, 165, 30]]
BOP_Purple = [[0, 0, 0], [148, 32, 148]]

# each of these makes a triangle in an RGB component plot.
# one component is always constant, the other two ramp up
# or down from 0 to 0.5 or 0.5 to 1
BMR_3C = [(0, 0, 1), (1, 0, 1), (1, 0, 0)]
CGY_3C = [(0, 1, 1), (0, 1, 0), (1, 1, 0)]
RMB_3C = [(1, 0, 0), (1, 0, 1), (0, 0, 1)]
YGC_3C = [(1, 1, 0), (0, 1, 0), (0, 1, 1)]

# TODO: this should be a string flag, like `_r` is for reversed
# this is a general thing, and we probably don't need these here.
I_Cyan = [(1, 1, 1), (0, 1, 1)]
I_Green = [(1, 1, 1), (0, 1, 0)]
I_Magenta = [(1, 1, 1), (1, 0, 1)]
I_Red = [(1, 1, 1), (1, 0, 0)]
I_Yellow = [(1, 1, 1), (1, 1, 0)]
I_Bordeaux = [(255, 255, 255), (204, 0, 51)]
I_Forest = [(255, 255, 255), (0, 153, 0)]

# I_Blue = [(1, 1, 1), (0, 0, 1)]  # Version in ChrisLuts
I_Blue = [[1, 1, 1], [0, 51 / 255, 204 / 255]]  # Version in napari
# these two are not in ChrisLuts... but they are in napari
I_Orange = [[1, 1, 1], [1, 117 / 255, 0]]
I_Purple = [[1, 1, 1], [117 / 255, 0, 1]]

# OPF LUTs are a set of 3 complementary LUTs (their overlay is white)
# that have orange (O), purple (P) and "fresh" green (F) as base colors.
OPF_Orange = [[0, 0, 0], [255, 117, 0]]
OPF_Purple = [[0, 0, 0], [117, 0, 255]]
OPF_Fresh = [[0, 0, 0], [0, 255, 117]]
