"""From https://github.com/imagej/imagej-common.

permalink:
https://github.com/imagej/imagej-common/tree/6da622e116e8ae34f951e167e2c36117b5417719/src/main/resources/luts.

Copyright (c) 2009 - 2022, ImageJ2 developers.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

# https://github.com/imagej/ImageJ/blob/1c6ff022cdc1b2ea6a8c5a5afdc14b0bc06583be/ij/plugin/LutLoader.java#L185-L187
fire = [
    [0, 0, 0],
    [0, 0, 61],
    [1, 0, 96],
    [25, 0, 130],
    [49, 0, 165],
    [73, 0, 192],
    [98, 0, 220],
    [122, 0, 227],
    [146, 0, 210],
    [162, 0, 181],
    [173, 0, 151],
    [184, 0, 122],
    [195, 0, 93],
    [207, 14, 64],
    [217, 35, 35],
    [229, 57, 5],
    [240, 79, 0],
    [252, 101, 0],
    [255, 117, 0],
    [255, 133, 0],
    [255, 147, 0],
    [255, 161, 0],
    [255, 175, 0],
    [255, 190, 0],
    [255, 205, 0],
    [255, 219, 0],
    [255, 234, 0],
    [255, 248, 35],
    [255, 255, 98],
    [255, 255, 160],
    [255, 255, 223],
    [255, 255, 255],
]

ice = [
    [0, 156, 140],
    [0, 165, 147],
    [0, 176, 158],
    [0, 184, 166],
    [0, 190, 170],
    [0, 196, 176],
    [19, 193, 209],
    [29, 184, 220],
    [50, 171, 234],
    [48, 162, 225],
    [79, 146, 236],
    [112, 125, 246],
    [134, 107, 250],
    [158, 93, 251],
    [186, 81, 250],
    [201, 87, 250],
    [217, 92, 245],
    [229, 97, 230],
    [242, 95, 230],
    [250, 93, 222],
    [250, 93, 202],
    [250, 90, 180],
    [250, 85, 163],
    [251, 69, 142],
    [250, 64, 123],
    [250, 54, 114],
    [250, 47, 106],
    [250, 35, 94],
    [251, 19, 84],
    [251, 0, 64],
    [243, 4, 26],
    [230, 0, 27],
]

HiLo = [
    (0.0, (0, 0, 1.0)),
    (0.002, (0, 0, 0)),  # for now, until we implement discontinuous colormaps
    (0.998, (1.0, 1.0, 1.0)),
    (1.0, (1.0, 0, 0)),
]

green_fire_blue = [
    (0, 0, 0),
    (0, 1 / 3, 2 / 3),
    (0, 1.0, 0),
    (1.0, 1.0, 0),
    (1.0, 1.0, 1.0),
]
