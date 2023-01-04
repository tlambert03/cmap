import re
from typing import Any, Sequence

from cmap import Colormap

# markdown tag for a single colormap: {{ cmap: name }}
CSS_CMAP = re.compile(r"{{\s?cmap:\s?([^}]+)\s?}}")

# the template for a single colormap
CMAP_DIV = """
<div class="cmap {class_list}" id="cmap-{name}">
    <div class="cmap-name">{name}</div>
    <div class="cmap-bar" style="{css}"></div>
</div>
"""


def _cmap_div(match: re.Match | str, class_list: Sequence[str] = ()) -> str:
    """Convert a `cmap` tag to a div with the colormap.

    {{ cmap: name }} -> <div class="cmap">
    """
    map_name = match if isinstance(match, str) else match[1].strip()
    cm = Colormap(map_name)
    css = cm.to_css().strip()
    return CMAP_DIV.format(name=map_name, css=css, class_list=" ".join(class_list))


def on_page_content(html: str, **kwargs: Any) -> str:
    html = CSS_CMAP.sub(_cmap_div, html)
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
