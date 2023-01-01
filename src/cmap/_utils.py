"""Utility functions and sample images for testing colormaps.

The sineramp and circlesineramp functions in this module are based on the MATLAB
functions of the same name, written by Peter Kovesi and available from his website
under the MIT License:

https://www.peterkovesi.com/matlabfns/
Copyright (c) 1995-2020 Peter Kovesi
pk@peterkovesi.com
"""


from typing import cast

import numpy as np


def sineramp(
    shape: tuple[int, int] | int = (256, 512),
    amp: float = 0.05,
    wavelen: float = 8,
    power: float = 2,
) -> np.ndarray:
    """Generate test image consisting of a sine wave superimposed on a ramp function.

    This function and all documentation is based on the MATLAB function of the same
    name, written by Peter Kovesi and available from his website:
    https://www.peterkovesi.com/matlabfns/

    Copyright (c) 1996-2005 Peter Kovesi
    School of Computer Science & Software Engineering
    The University of Western Australia

    The test image consists of a sine wave superimposed on a ramp function The
    amplitude of the sine wave is modulated from its full value at the top of the
    image to 0 at the bottom.

    The image is useful for evaluating the effectiveness of different color maps.
    Ideally the sine wave pattern should be equally discernible over the full
    range of the color map.  In addition, across the bottom of the image, one
    should not see any identifiable features as the underlying signal is a smooth
    ramp.  In practice many color maps have uneven perceptual contrast over their
    range and often include 'flat spots' of no perceptual contrast that can hide
    significant features.

    Parameters
    ----------
    shape : tuple, optional
        [rows cols] specifying size of test image.  If a single value is supplied
        the image is square. Defaults to [256 512];  Note the number of columns is
        nominal and will be ajusted so that there are an integer number of sine wave
        cycles across the image.
    amp : float, optional
        Amplitude of sine wave. Defaults to 12.5
    wavelen : float, optional
        Wavelength of sine wave in pixels. Defaults to 8.
    power : float, optional
        Power to which the linear attenuation of amplitude, from top to bottom, is
        raised.  For no attenuation use p = 0.  For linear attenuation use a value
        of 1.  For contrast sensitivity experiments use larger values of p.  The
        default value is 2.

    Returns
    -------
    im : ndarray
        Test image
    """
    if isinstance(shape, int):
        rows = cols = shape
    elif len(shape) == 2:
        rows, cols = shape
    else:  # pragma: no cover
        raise ValueError("size must be a 1 or 2 element vector")

    # Adjust width of image so that we have an integer number of cycles of
    # the sinewave.  This is helps should one be using the test image to
    # evaluate a cyclic colour map.  However you will still see a slight
    # cyclic discontinuity at the top of the image, though this will
    # disappear at the bottom of the test image
    cycles = round(cols / wavelen)
    cols = int(cycles * wavelen)

    # Sine wave
    x = np.arange(cols)
    fx = amp * np.sin(1 / wavelen * 2 * np.pi * x)

    # Vertical modulating function
    A = (np.arange(rows - 1, -1, -1) / (rows - 1)) ** power
    im = A[:, np.newaxis] * fx

    # Add ramp
    ramp = np.arange(cols)[np.newaxis, :] / (cols - 1)
    im = im + ramp * (-2 * amp)

    # Now normalise each row so that it spans the full data range from 0 to 1.
    # This ensures that, at the lower edge of the image, the full colour map is
    # displayed.  It also helps with the evaluation of cyclic colour maps though
    # a small cyclic discontinuity will remain at the top of the test image.
    for r in range(rows):
        row_data = im[r, :]
        row_data -= row_data.min()
        row_data /= row_data.max()
        im[r, :] = row_data
    return cast("np.ndarray", im)


def circlesineramp(
    size: int = 512,
    amp: float = np.pi / 10,
    wavelen: float = 8,
    power: float = 2,
    hole: bool = True,
) -> np.ndarray:
    """Generate test image for evaluating cyclic color maps.

    This function and all documentation is based on the MATLAB function of the same
    name, written by Peter Kovesi and available from his website:
    https://www.peterkovesi.com/matlabfns/

    Copyright (c) 1996-2005 Peter Kovesi
    School of Computer Science & Software Engineering
    The University of Western Australia

    The test image is a circular pattern consistsing of a sine wave superimposed
    on a spiral ramp function.  The spiral ramp starts at a value of 0 pointing
    right, increasing anti-clockwise to a value of 2*pi as it completes the full
    circle. This gives a 2*pi discontinuity on the right side of the image.  The
    amplitude of the superimposed sine wave is modulated from its full value at
    the outside of the circular pattern to 0 at the centre.  The default sine wave
    amplitude of pi/10 means that the overall size of the sine wave from peak to
    trough represents 2*(pi/10)/(2*pi) = 10% of the total spiral ramp of 2*pi.  If
    you are testing your colour map over a cycle of pi you should use amp = pi/20
    to obtain an equivalent ratio of sine wave to circular ramp.

    The image is designed for evaluating the effectiveness of cyclic colour maps.
    It is the cyclic companion to `sineramp`.  Ideally the sine wave pattern should
    be equally discernible over all angles around the test image.  In practice
    many colourmaps have uneven perceptual contrast over their range and often
    include 'flat spots' of no perceptual contrast that can hide significant
    features (e.g. hsv colour map).

    Parameters
    ----------
    size : int, optional
        Size of one side of the test image.  Defaults to 512.
    amp : float, optional
        Amplitude of sine wave. Defaults to 12.5
    wavelen : float, optional
        Wavelength of sine wave in pixels. Defaults to 8.
    power : float, optional
        Power to which the linear attenuation of amplitude, from top to bottom, is
        raised.  For no attenuation use p = 0.  For linear attenuation use a value
        of 1.  For contrast sensitivity experiments use larger values of p.  The
        default value is 2.
    hole : bool, optional
        If True, the test image will have a hole in the centre.  Defaults to True.

    Returns
    -------
    np.ndarray
        Test image of size (size, size) with values in the range 0-2*pi.
    """
    # Set values for inner and outer radii of test pattern
    maxr = size / 2 * 0.9
    minr = 0.15 * size if hole else 0

    # Determine number of cycles to achieve desired wavelength at half radius
    meanr = (maxr + minr) / 2
    circum = 2 * np.pi * meanr
    cycles = round(circum / wavelen)

    # Angles are +ve anticlockwise and mod 2*pi
    indices = np.arange(0, size) - size / 2
    x, y = np.meshgrid(indices, indices)
    theta = np.mod(np.arctan2(-y, x), 2 * np.pi)
    rad = np.sqrt(x**2 + y**2)

    # Normalise radius so that it varies 0-1 over minr to maxr
    rad = (rad - minr) / (maxr - minr)

    # Form the image
    im = amp * rad**power * np.sin(cycles * theta) + theta

    # Ensure all values are within 0-2*pi so that a simple default display
    # with a cyclic colour map will render the image correctly.
    im = np.mod(im, 2 * np.pi)

    # 'Nanify' values outside normalised radius values of 0-1
    alpha = np.ones_like(im)
    im[rad > 1] = np.nan
    alpha[rad > 1] = 0

    if hole:
        im[rad < 0] = np.nan
        alpha[rad < 0] = 0

    return cast(np.ndarray, im * alpha)
