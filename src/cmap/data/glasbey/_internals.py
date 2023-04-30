# type: ignore
# glasbey vendored from https://github.com/lmcinnes/glasbey.
# see __init__ and LICENSE_GLASBEY
import numpy as np

# "numbafication" is done at the bottom of the module


def get_next_color(distances, colors, new_color):
    argmax = -1
    max_dist = 0.0
    dim = distances.shape[0]
    for i in range(dim):
        d = 0.0
        for j in range(3):
            diff = colors[i, j] - new_color[j]
            d += diff * diff
        if d < distances[i]:
            distances[i] = d
        if distances[i] > max_dist:
            max_dist = distances[i]
            argmax = i

    return colors[argmax]


def generate_palette_cam02ucs(colors, initial_palette, size):
    distances = np.full(colors.shape[0], fill_value=1e12, dtype=np.float32)
    result = np.empty((size, 3), dtype=np.float32)
    initial_palette_size = np.uint16(initial_palette.shape[0])
    result[:initial_palette_size] = initial_palette

    for i in range(initial_palette_size):
        _ = get_next_color(distances, colors, result[i])

    for i in range(initial_palette_size, size):
        result[i] = get_next_color(distances, colors, result[i - 1])

    return result


def two_space_get_next_color(
    distances, colors1, colors2, new_color1, new_color2, alpha=0.0
):
    argmax = -1
    max_dist = 0.0
    dim = distances.shape[0]
    for i in range(dim):
        # Color space 1 distance
        d1 = 0.0
        if alpha > 0.0:
            for j in range(3):
                diff = colors1[i, j] - new_color1[j]
                d1 += diff * diff

        # Color space 2 distance
        d2 = 0.0
        if alpha < 1.0:
            for j in range(colors2.shape[1]):
                diff = colors2[i, j] - new_color2[j]
                d2 += diff * diff

        # Combined distance
        d = alpha * d1 + (1.0 - alpha) * d2

        if d < distances[i]:
            distances[i] = d
        if distances[i] > max_dist:
            max_dist = distances[i]
            argmax = i

    return colors1[argmax], colors2[argmax]


def generate_palette_cam02ucs_and_other(
    colors1, colors2, initial_palette1, initial_palette2, size, alpha=0.0
):
    distances = np.full(colors1.shape[0], fill_value=1e12, dtype=np.float32)
    result = np.empty((size, 3), dtype=np.float32)
    initial_palette_size = np.uint16(initial_palette1.shape[0])
    result[:initial_palette_size] = initial_palette1

    for i in range(initial_palette_size):
        _ = two_space_get_next_color(
            distances,
            colors1,
            colors2,
            result[i],
            initial_palette2[i],
            alpha=alpha,
        )

    next_color_other_space = initial_palette2[-1]

    for i in range(initial_palette_size, size):
        result[i], next_color_other_space = two_space_get_next_color(
            distances,
            colors1,
            colors2,
            result[i - 1],
            next_color_other_space,
            alpha=alpha,
        )

    return result


try:
    import numba
except ImportError:
    import warnings

    warnings.warn(
        "Numba not installed. glasbey palette creation will be slow.", stacklevel=2
    )
else:
    jit1 = numba.njit(
        [
            "f4[::1](f4[::1], f4[:,::1], f4[::1])",
            numba.types.Array(numba.float32, 1, "C", readonly=True)(
                numba.types.Array(numba.float32, 1, "C"),
                numba.types.Array(numba.float32, 2, "C", readonly=True),
                numba.types.Array(numba.float32, 1, "C", readonly=True),
            ),
        ],
        locals={
            "diff": numba.float32,
            "d": numba.float32,
            "dim": numba.intp,
            "i": numba.uint32,
        },
        fastmath=True,
        nogil=True,
        boundscheck=False,
        cache=True,
    )

    # get_next_color(distances, colors, new_color)
    get_next_color = jit1(get_next_color)

    jit2 = numba.njit(
        [
            "f4[:,::1](f4[:,::1], f4[:,::1], i4)",
            numba.types.Array(numba.float32, 2, "C")(
                numba.types.Array(numba.float32, 2, "C", readonly=True),
                numba.types.Array(numba.float32, 2, "C", readonly=True),
                numba.uint32,
            ),
        ],
        locals={
            "distances": numba.types.Array(numba.float32, 1, "C"),
            "initial_palette_size": numba.uint16,
            "i": numba.uint16,
        },
        cache=True,
    )

    # generate_palette_cam02ucs(colors, initial_palette, size)
    generate_palette_cam02ucs = jit2(generate_palette_cam02ucs)

    jit4 = numba.njit(
        [
            "UniTuple(f4[::1], 2)(f4[::1], f4[:, ::1], f4[:, ::1], f4[::1], f4[::1], f4)",
            numba.types.UniTuple(
                numba.types.Array(numba.float32, 1, "C", readonly=True), 2
            )(
                numba.types.Array(numba.float32, 1, "C"),
                numba.types.Array(numba.float32, 2, "C", readonly=True),
                numba.types.Array(numba.float32, 2, "C", readonly=True),
                numba.types.Array(numba.float32, 1, "C", readonly=True),
                numba.types.Array(numba.float32, 1, "C", readonly=True),
                numba.float32,
            ),
        ],
        locals={
            "diff": numba.float32,
            "d1": numba.float32,
            "d2": numba.float32,
            "d": numba.float32,
            "dim": numba.intp,
            "i": numba.uint32,
        },
        fastmath=True,
        nogil=True,
        boundscheck=False,
        cache=True,
    )

    two_space_get_next_color = jit4(two_space_get_next_color)

    jit5 = numba.njit(
        [
            "f4[:,::1](f4[:,::1], f4[:,::1], f4[:,::1], f4[:,::1], i4, f4)",
            numba.types.Array(numba.float32, 2, "C")(
                numba.types.Array(numba.float32, 2, "C", readonly=True),
                numba.types.Array(numba.float32, 2, "C", readonly=True),
                numba.types.Array(numba.float32, 2, "C", readonly=True),
                numba.types.Array(numba.float32, 2, "C", readonly=True),
                numba.uint32,
                numba.float32,
            ),
        ],
        locals={
            "distances": numba.types.Array(numba.float32, 1, "C"),
            "initial_palette_size": numba.uint16,
            "i": numba.uint16,
        },
        cache=True,
    )

    generate_palette_cam02ucs_and_other = jit5(generate_palette_cam02ucs_and_other)
