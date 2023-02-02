from __future__ import annotations

from typing import cast

import numpy as np

CUBE_ROT = np.array([[-0.14861, 1.78277], [-0.29227, -0.90649], [1.97294, 0.0]])


def cubehelix(
    X: np.ndarray | int,
    start: float = 0.5,
    rotation: float = -1.5,
    gamma: float = 1.0,
    sat: float | np.ndarray = 1.0,
    reverse: bool = False,
) -> np.ndarray:
    """Create Cubehelix colors.

    http://adsabs.harvard.edu/abs/2011arXiv1108.5083G
    """
    x = np.linspace(0, 1, X) if isinstance(X, int) else np.asarray(X)
    if isinstance(sat, np.ndarray) and len(sat) != len(x):  # pragma: no cover
        raise ValueError("sat must be a scalar or an array of the same length as X")

    # apply the gamma correction
    xg = x**gamma

    # Calculate amplitude and angle of deviation from the black to white
    # diagonal in the plane of constant perceived intensity.
    # Amplitude of helix from grayscale map
    amp = sat * xg * (1.0 - xg) / 2.0
    # Rotation angle
    phi = 2.0 * np.pi * (start / 3.0 + rotation * x)

    # Compute the RGB vectors according to Green 2011 Eq 2
    sin_cos = np.array([np.cos(phi), np.sin(phi)])
    rgb = (xg + amp * np.dot(CUBE_ROT, sin_cos)).T

    # Clipping is necessary in some cases when sat > 1
    np.clip(rgb, 0.0, 1, out=rgb)
    return cast("np.ndarray", rgb[::-1] if reverse else rgb)
