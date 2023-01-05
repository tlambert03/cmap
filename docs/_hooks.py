from functools import partial
import json
import re
from typing import Any, Sequence

import numpy as np
from cmap import RGBA, Colormap, _util

# markdown tag for a single colormap: {{ cmap: name }}
CSS_CMAP = re.compile(r"{{\s?cmap:\s?([^}^\s]+)\s?(\d+)?\s?}}")
CSS_CMAP_GRAY = re.compile(r"{{\s?cmap_gray:\s?([^}^\s]+)\s?(\d+)?\s?}}")
CMAP_LINEARITY = re.compile(r"{{\s?cmap_linearity:\s?([^}]+)\s?}}")
CMAP_RGB = re.compile(r"{{\s?cmap_rgb:\s?([^}]+)\s?}}")

# the template for a single colormap
CMAP_DIV = """
<a href="{url}">
<div class="cmap {class_list}" id="cmap-{name}">
    <div class="cmap-name">{name}</div>
    <div class="cmap-bar" style="{css}"></div>
</div>
</a>
"""


CMAP_LINEARITY_PLOT = """
<canvas id="{name}-linearity-chart" width="800" height="350"></canvas>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.1.1/chart.umd.min.js" integrity="sha512-RnIvaWVgsDUVriCOO7ZbDOwPqBY1kdE8KJFmJbCSFTI+a+/s+B1maHN513SFhg1QwAJdSKbF8t2Obb8MIcTwxA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script>
new Chart(document.getElementById("{name}-linearity-chart"), {{
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

# NOTE: we're not adding the chart.js src here, meaning this has to be used after the
# linearity plot above...
CMAP_RGB_PLOT = """
<canvas id="{name}-rgb-chart" width="800" height="350"></canvas>
<script>
new Chart(document.getElementById("{name}-rgb-chart"), {{
    type: 'line',
    data: {{    
        labels: {labels},
        datasets: [
            {{label: "red", borderColor: "#FF0000BB", data: {rdata} }},
            {{label: "green", borderColor: "#00AA00BB", data: {gdata} }},
            {{label: "blue", borderColor: "#0000FFBB", data: {bdata} }}
        ]
    }},
    options: {{
        scales: {{
            y: {{ title: {{ text: "Component Value", display: true}} }},
            x: {{ 
                ticks: {{ 
                    callback: function(val, index) {{
                        return index % 10 === 0 ? this.getLabelForValue(val) : '';
                    }},
                    maxTicksLimit: 11,
                    autoSkip: false,
                    maxRotation: 0,
                }},
            }}
        }},
        plugins: {{legend: {{display: false}} }},
        elements: {{point: {{radius: 0}}, line: {{borderWidth: 4}} }},
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
    url = f'/cmap/cmaps/{cm.category}/{map_name.replace("_r", "")}/'
    if isinstance(match, re.Match) and match[2] is not None:
        css += f" height: {match[2]}px;"
    return CMAP_DIV.format(
        name=map_name, css=css, class_list=" ".join(class_list), url=url
    )


def _cmap_linearity_plot(match: re.Match, N: int = 101) -> str:
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
        name=cmap_name, data=json.dumps(data), colors=json.dumps(colors), radius=12
    )


def _cmap_rgb_plot(match: re.Match) -> str:
    """Convert a `cmap_rgb` tag to a plot of the colormap RGB values."""
    cmap_name = match[1].strip()
    cm = Colormap(cmap_name)
    N = 101
    x = np.linspace(0.0, 1.0, N)
    colors = cm(x, N=N)
    rdata = json.dumps(colors[:, 0].tolist())
    gdata = json.dumps(colors[:, 1].tolist())
    bdata = json.dumps(colors[:, 2].tolist())
    return CMAP_RGB_PLOT.format(
        name=cmap_name,
        labels=json.dumps([round(i, 2) for i in x]),
        rdata=rdata,
        gdata=gdata,
        bdata=bdata,
    )


def on_page_content(html: str, **kwargs: Any) -> str:
    html = CSS_CMAP.sub(_cmap_div, html)
    html = CSS_CMAP_GRAY.sub(partial(_cmap_div, class_list=['grayscale']), html)
    html = CMAP_LINEARITY.sub(_cmap_linearity_plot, html)
    html = CMAP_RGB.sub(_cmap_rgb_plot, html)
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
