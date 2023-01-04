# Colormap Catalog

To use any colormap in the catalog, you can pass its name to the [`Colormap`][cmap.Colormap]
constructor:

```python
from cmap import Colormap

cmap = Colormap('viridis')
```

See the [Colormap API docs](api/colormap.md) for more details.
See the [cookbook](cookbook.md) for usage examples.

<!--
With that object you can do things like:

```python
# call it directly to colorize an ndarray of values
# values should be (pre-normalized to 0-1)
img = np.random.random((24, 24))
colored = cmap(img)
assert colored.shape == (24, 24, 4)

# use it in matplotlib
import matplotlib.pyplot as plt
plt.imshow(img, cmap=cmap.to_mpl())

# use it in napari
from napari import view_image
view_image(img, colormap=cmap.to_napari())
``` -->

## Colormaps by category

{{ CMAP_CATALOG }}
