from pathlib import Path

import mkdocs_gen_files
import pandas as pd
from cmap import Colormap
from cmap._catalog import catalog
from cmap._util import report

TEMPLATE = """# {name}

| category | license | source |
| --- | --- | --- |
| {category} | {license} | {source} |

```python
from cmap import Colormap

cm = Colormap('{name}')  # case insensitive
```

{{{{ cmap: {name} 40 }}}}
{{{{ cmap_gray: {name} 40 }}}}
{{{{ cmap_sineramp: {name} }}}}

## Perceptual Lightness

<canvas class="linearity-chart cmap-chart" data-cmap-name="{name}" width="800" height="350"></canvas>
<p style="text-align: center;">
<em style="font-size: small; color: gray;">
L* measured in
<a href="https://onlinelibrary.wiley.com/doi/10.1002/col.20227">CAM02 Uniform Color Space (CAM02-UCS)</a>
</em>
</p>

## RGB components

<canvas class="rgb-chart cmap-chart" data-cmap-name="{name}" width="800" height="350"></canvas>

## Hue & Saturation

<canvas class="hsl-chart cmap-chart" data-cmap-name="{name}" width="800" height="350"></canvas>
"""

DOCS = Path(__file__).parent
LICENSE_URL = {
    "CC0": "https://creativecommons.org/publicdomain/zero/1.0/",
    "Apache-2.0": "https://www.apache.org/licenses/LICENSE-2.0",
    "MIT": "https://opensource.org/licenses/MIT",
    "BSD-3-Clause": "https://opensource.org/licenses/BSD-3-Clause",
    "BSD-2-Clause": "https://opensource.org/licenses/BSD-2-Clause",
}

for name in catalog:
    info = catalog[name]
    category = info["category"]
    output = f"catalog/{category}/{name}.md"
    license_: str = info["license"]
    source = info.get("source", "...")
    if license_ in LICENSE_URL:
        license_ = f"[{license_}]({LICENSE_URL[license_]})"
    with mkdocs_gen_files.open(f"data/{name}.json", "w") as f:
        cm = Colormap(name)
        pd.DataFrame(report(cm)).to_json(f, orient="records")
    with mkdocs_gen_files.open(f"catalog/{category}/{name}.md", "w") as f:
        f.write(
            TEMPLATE.format(
                name=name, category=category, license=license_, source=source
            )
        )
