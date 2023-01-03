import numpy as np

gray = [(0, 0, 0), (1, 1, 1)]
autumn = [(1, 0, 0), (1, 1, 0)]
[
    (0.0, (0.0, 0.0, 0.0, 1.0)),
    (0.365079, (0.31944412499999997, 0.319444, 0.444444, 1.0)),
    (0.746032, (0.652778, 0.777778, 0.7777779500000788, 1.0)),
    (1.0, (1.0, 1.0, 1.0, 1.0)),
]
bone = [
    (0.0, (0.0, 0.0, 0.0, 1.0)),
    (0.365079, (0.31944412499999997, 0.319444, 0.444444, 1.0)),
    (0.746032, (0.652778, 0.777778, 0.7777779500000788, 1.0)),
    (1.0, (1.0, 1.0, 1.0, 1.0)),
]
cool = [(0, 1, 1), (1, 0, 1)]
copper = [
    (0.0, (0.0, 0.0, 0.0, 1)),
    (0.809524, (1.0, 0.6324001488000001, 0.40273819, 1)),
    (1.0, (1.0, 0.7812, 0.4975, 1)),
]
hot = [
    (0.0, (0.0416, 0.0, 0.0, 1.0)),
    (0.365079, (1.0, 0.0, 0.0, 1.0)),
    (0.746032, (1.0, 1.0, 0.0, 1.0)),
    (1.0, (1.0, 1.0, 1.0, 1.0)),
]
hsv = [
    (0.0, (1.0, 0.0, 0.0, 1.0)),
    (0.15873, (1.0, 0.9375, 0.0, 1.0)),
    (0.174603, (0.96875, 1.0, 0.0, 1.0)),
    (0.333333, (0.03125, 1.0, 0.0, 1.0)),
    (0.349206, (0.0, 1.0, 0.0625, 1.0)),
    (0.507937, (0.0, 1.0, 1.0, 1.0)),
    (0.666667, (0.0, 0.0625, 1.0, 1.0)),
    (0.68254, (0.03125, 0.0, 1.0, 1.0)),
    (0.84127, (0.96875, 0.0, 1.0, 1.0)),
    (0.857143, (1.0, 0.0, 0.9375, 1.0)),
    (1.0, (1.0, 0.0, 0.09375, 1.0)),
]

jet = [
    (0.0, (0.0, 0.0, 0.5, 1.0)),
    (0.11, (0.0, 0.0, 1.0, 1.0)),
    (0.125, (0.0, 0.0, 1.0, 1.0)),
    (0.34, (0.0, 0.86, 1.0, 1.0)),
    (0.35, (0.0, 0.9, 0.9677419354838711, 1.0)),
    (0.375, (0.08064516129032263, 1.0, 0.8870967741935485, 1.0)),
    (0.64, (0.9354838709677419, 1.0, 0.032258064516129004, 1.0)),
    (0.65, (0.9677419354838709, 0.9629629629629629, 0.0, 1.0)),
    (0.66, (1.0, 0.9259259259259258, 0.0, 1.0)),
    (0.89, (1.0, 0.07407407407407418, 0.0, 1.0)),
    (0.91, (0.909090909090909, 0.0, 0.0, 1.0)),
    (1.0, (0.5, 0.0, 0.0, 1.0)),
]

spring = [(1, 0, 1), (1, 1, 0)]
summer = [(0, 0.5, 0.4), (1, 1, 0.4)]
winter = [(0.0, 0.0, 1.0), (0.0, 1.0, 0.5)]
pink = [
    (0.1178, 0.0, 0.0),
    (0.195857, 0.102869, 0.102869),
    (0.250661, 0.145479, 0.145479),
    (0.295468, 0.178174, 0.178174),
    (0.334324, 0.205738, 0.205738),
    (0.369112, 0.230022, 0.230022),
    (0.400892, 0.251976, 0.251976),
    (0.430331, 0.272166, 0.272166),
    (0.457882, 0.290957, 0.290957),
    (0.483867, 0.308607, 0.308607),
    (0.508525, 0.3253, 0.3253),
    (0.532042, 0.341178, 0.341178),
    (0.554563, 0.356348, 0.356348),
    (0.576204, 0.370899, 0.370899),
    (0.597061, 0.3849, 0.3849),
    (0.617213, 0.39841, 0.39841),
    (0.636729, 0.411476, 0.411476),
    (0.655663, 0.424139, 0.424139),
    (0.674066, 0.436436, 0.436436),
    (0.69198, 0.448395, 0.448395),
    (0.709441, 0.460044, 0.460044),
    (0.726483, 0.471405, 0.471405),
    (0.743134, 0.482498, 0.482498),
    (0.759421, 0.493342, 0.493342),
    (0.766356, 0.517549, 0.503953),
    (0.773229, 0.540674, 0.514344),
    (0.780042, 0.562849, 0.524531),
    (0.786796, 0.584183, 0.534522),
    (0.793492, 0.604765, 0.544331),
    (0.800132, 0.624669, 0.553966),
    (0.806718, 0.643958, 0.563436),
    (0.81325, 0.662687, 0.57275),
    (0.81973, 0.6809, 0.581914),
    (0.82616, 0.698638, 0.590937),
    (0.832539, 0.715937, 0.599824),
    (0.83887, 0.732828, 0.608581),
    (0.845154, 0.749338, 0.617213),
    (0.851392, 0.765493, 0.625727),
    (0.857584, 0.781313, 0.634126),
    (0.863731, 0.796819, 0.642416),
    (0.869835, 0.812029, 0.6506),
    (0.875897, 0.82696, 0.658682),
    (0.881917, 0.841625, 0.666667),
    (0.887896, 0.85604, 0.674556),
    (0.893835, 0.870216, 0.682355),
    (0.899735, 0.884164, 0.690066),
    (0.905597, 0.897896, 0.697691),
    (0.911421, 0.911421, 0.705234),
    (0.917208, 0.917208, 0.727166),
    (0.922958, 0.922958, 0.748455),
    (0.928673, 0.928673, 0.769156),
    (0.934353, 0.934353, 0.789314),
    (0.939999, 0.939999, 0.808969),
    (0.945611, 0.945611, 0.828159),
    (0.95119, 0.95119, 0.846913),
    (0.956736, 0.956736, 0.865261),
    (0.96225, 0.96225, 0.883229),
    (0.967733, 0.967733, 0.900837),
    (0.973185, 0.973185, 0.918109),
    (0.978607, 0.978607, 0.935061),
    (0.983999, 0.983999, 0.951711),
    (0.989361, 0.989361, 0.968075),
    (0.994695, 0.994695, 0.984167),
    (1.0, 1.0, 1.0),
]
# prism


def flag(x: np.ndarray) -> np.ndarray:
    """Flag colormap."""
    r = 0.75 * np.sin((x * 31.5 + 0.25) * np.pi) + 0.5
    g = np.sin(x * 31.5 * np.pi)
    b = 0.75 * np.sin((x * 31.5 - 0.25) * np.pi) + 0.5
    return np.stack([r, g, b], axis=-1)


def prism(x: np.ndarray) -> np.ndarray:
    """Prism colormap."""
    r = 0.75 * np.sin((x * 20.9 + 0.25) * np.pi) + 0.67
    g = 0.75 * np.sin((x * 20.9 - 0.25) * np.pi) + 0.33
    b = -1.1 * np.sin((x * 20.9) * np.pi)
    return np.stack([r, g, b], axis=-1)
