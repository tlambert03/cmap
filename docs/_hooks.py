import json
import re
from typing import Any, Sequence

import numpy as np
from cmap import RGBA, Colormap, _util

# markdown tag for a single colormap: {{ cmap: name }}
CSS_CMAP = re.compile(r"{{\s?cmap:\s?([^}]+)\s?}}")
CMAP_LINEARITY = re.compile(r"{{\s?cmap_linearity:\s?([^}]+)\s?}}")

# the template for a single colormap
CMAP_DIV = """
<div class="cmap {class_list}" id="cmap-{name}">
    <div class="cmap-name">{name}</div>
    <div class="cmap-bar" style="{css}"></div>
</div>
"""


CMAP_LINEARITY_PLOT = """
<canvas id="bar-chart" width="800" height="450"></canvas>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.1.1/chart.umd.min.js" integrity="sha512-RnIvaWVgsDUVriCOO7ZbDOwPqBY1kdE8KJFmJbCSFTI+a+/s+B1maHN513SFhg1QwAJdSKbF8t2Obb8MIcTwxA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script>
new Chart(document.getElementById("bar-chart"), {{
    type: 'scatter',
    data: {{
        datasets: [{{backgroundColor: {colors}, data: {data}}}]
    }},
    options: {{
        scales: {{y: {{ title: {{ text: "Lightness 𝐿*", display: true}} }} }},
        plugins: {{legend: {{display: false}} }},
        elements: {{point: {{radius: {radius}, borderWidth: 0}} }},
    }}
}});
</script>
"""


def _cmap_div(match: re.Match | str, class_list: Sequence[str] = ()) -> str:
    """Convert a `cmap` tag to a div with the colormap.

    {{ cmap: name }} -> <div class="cmap">
    """
    map_name = match if isinstance(match, str) else match[1].strip()
    cm = Colormap(map_name)
    css = cm.to_css().strip()
    return CMAP_DIV.format(name=map_name, css=css, class_list=" ".join(class_list))


def _cmap_linearity(match: re.Match, N: int = 100) -> str:
    """Convert a `cmap_linearity` tag to a plot of the colormap linearity."""
    cmap_name = match[1].strip()
    cm = Colormap(cmap_name)
    data = []
    colors = []

    x = np.linspace(0.0, 1.0, N)
    lab = _util.calc_lightness(cm, x)

    data = [{"x": round(a, 2), "y": round(b, 2)} for a, b in zip(x, lab)]
    colors = [RGBA(*c).to_hex() for c in cm(x)]
    return CMAP_LINEARITY_PLOT.format(
        data=json.dumps(data), colors=json.dumps(colors), radius=12
    )


def on_page_content(html: str, **kwargs: Any) -> str:
    html = CSS_CMAP.sub(_cmap_div, html)
    html = CMAP_LINEARITY.sub(_cmap_linearity, html)
    if "{{ CMAP_CATALOG }}" in html:
        html = html.replace(r"{{ CMAP_CATALOG }}", _cmap_catalog())
    return html


def _cmap_catalog() -> str:
    """Return the HTML for the colormap catalog page.

    this works in conjunction with the `javascripts/extra.js` script.
    """
    from cmap._catalog import CATALOG

    categories = set()
    lines = []
    for cmap_name, details in sorted(CATALOG.items(), key=lambda x: x[0].lower()):
        category = details.get("category") or "Uncategorized"
        categories.add(category)
        classes = ["filterDiv"] + [category.lower()]
        lines.append(_cmap_div(cmap_name, classes))

    btns = [
        '<div id="cmapFilterButtons">',
        """<button class="btn active" onclick="filterSelection('all')">All</button>""",
    ]
    btns.extend(
        f'<button class="btn" onclick="filterSelection({c.lower()!r})">{c}</button>'
        for c in sorted(categories)
    )
    btns.append("</div>")
    lines = btns + lines

    return "\n".join(lines)
