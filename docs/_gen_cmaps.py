from pathlib import Path

import mkdocs_gen_files
from cmap._catalog import catalog

DOCS = Path(__file__).parent
TEMPLATE = """# {name}

- Category: `{category}`

- License: `{license}`

- Source: ...

```python
from cmap import Colormap

cm = Colormap({name!r})  # case insensitive
```

{{{{ cmap: {name} 40 }}}}
{{{{ cmap_gray: {name} 40 }}}}
{{{{ cmap_sineramp: {name} }}}}

### Perceptual Lightness

<p style="text-align: center;">
<em style="font-size: small; color: gray;">
L* measured in
<a href="https://onlinelibrary.wiley.com/doi/10.1002/col.20227">CAM02 Uniform Color Space (CAM02-UCS)</a>
</em>
</p>

{{{{ cmap_linearity: {name} }}}}

### RGB components

{{{{ cmap_rgb: {name} }}}}
"""

for name in ("jet",):
    info = catalog[name]
    category = info["category"]
    output = f"catalog/{category}/{name}.md"
    with mkdocs_gen_files.open(f"catalog/{category}/{name}.md", "w") as f:
        f.write(TEMPLATE.format(name=name, category=category, license=info["license"]))
    # mkdocs_gen_files.set_edit_path(filename, "gen_pages.py")
