import base64
import io
import re
from functools import partial
from typing import Any, Sequence

import numpy as np
from cmap import Colormap, _util
from cmap._color import NAME_TO_RGB

# the template for a single colormap
CMAP_DIV = """
<div class="cmap {class_list}" id="cmap-{name}">
    <div class="cmap-name">{name}</div>
    <div class="cmap-bar" style="{css}"></div>
</div>
"""
CMAP_LINK = '<a href="{url}">' + CMAP_DIV + "</a>"


def _cmap_div(match: re.Match | str, class_list: Sequence[str] = ()) -> str:
    """Convert a `cmap` tag to a div with the colormap.

    {{ cmap: name }} -> <div class="cmap">
    """
    map_name = match if isinstance(match, str) else match[1].strip()
    cm = Colormap(map_name)
    css = cm.to_css().strip()
    url = f'/cmap/catalog/{cm.category}/{map_name.replace("_r", "")}/'
    if isinstance(match, re.Match) and match[2] is not None:
        css += f" height: {match[2]}px;"
    return CMAP_LINK.format(
        name=map_name, css=css, class_list=" ".join(class_list), url=url
    )


def _cmap_expr(match: re.Match) -> str:
    """Convert a `cmap_expr` tag to a div with the colormap.

    {{ cmap_expr: {0: 'blue', 0.5: 'yellow', 1: 'red'} }} -> <div class="cmap">...
    """
    map_name = match[1].strip()
    cm = Colormap(eval(map_name))
    css = cm.to_css().strip()
    return CMAP_DIV.format(name="", css=css, class_list="cmap-expr")


SINERAMP = _util.sineramp((128, 512))[:, ::-1]


def _cmap_sineramp(match: re.Match) -> str:
    """Convert a `cmap_sineramp` tag to an img element with sineramp applied.

    {{ cmap_sineramp: viridis }} -> <img class="cmap">...
    """
    import imageio

    map_name = match[1].strip()
    cm = Colormap(map_name)
    img = (cm(SINERAMP) * 255).astype(np.uint8)
    with io.BytesIO() as f:
        imageio.imwrite(f, img, format="png")  # type: ignore
        data = base64.b64encode(f.getvalue()).decode("ascii")
    alt = f"sineramp with {map_name} colormap applied"
    return f'<img style="height: 128px" width="100%" src="data:image/png;base64, {data}" alt="{alt}" />'


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


COLORBOX = """<div class="colorbox" style="background-color: {hex}; color: {text_color}">
    <strong class="colornamespan">{name}</strong><br />
    <span class="colorhexspan">{hex}</span><br />
    <span class="colortuple">{rgb}</span><br />
</div>
"""


def _color_list() -> str:
    """Return the HTML for the color list page."""
    colors = []
    for name, c in NAME_TO_RGB.items():
        if (hsl := c.to_hsl()).l == 0.5:
            text_color = "#000" if hsl.h <= 0.5 else "#FFF"
        else:
            text_color = "#000" if hsl.l > 0.50 or not c.a else "#FFF"
        cbox = COLORBOX.format(
            name=name,
            hex=c.to_hex(),
            text_color=text_color,
            rgb=c.rgba_string(),
        )
        colors.append(cbox)
    return '<div class="colorlist">{}</div>'.format("\n".join(colors))


# -----------------------------------------------------------------------------
# mkdocs hooks
# -----------------------------------------------------------------------------
# markdown tag for a single colormap: {{ cmap: name }}
CSS_CMAP = re.compile(r"{{\s?cmap:\s?([^}^\s]+)\s?(\d+)?\s?}}")
CSS_CMAP_GRAY = re.compile(r"{{\s?cmap_gray:\s?([^}^\s]+)\s?(\d+)?\s?}}")
CMAP_SINERAMP = re.compile(r"{{\s?cmap_sineramp:\s?([^}]+)\s?}}")
CMAP_EXPR = re.compile(r"{{\s?cmap_expr:\s(.+)\s}}")
CMAP_CATALOG = r"{{ CMAP_CATALOG }}"
COLOR_LIST = r"{{ COLOR_LIST }}"


def on_page_content(html: str, **kwargs: Any) -> str:
    html = CSS_CMAP.sub(_cmap_div, html)
    html = CSS_CMAP_GRAY.sub(partial(_cmap_div, class_list=["grayscale"]), html)
    html = CMAP_EXPR.sub(_cmap_expr, html)
    html = CMAP_SINERAMP.sub(_cmap_sineramp, html)
    if CMAP_CATALOG in html:
        html = html.replace(CMAP_CATALOG, _cmap_catalog())
    if COLOR_LIST in html:
        html = html.replace(COLOR_LIST, _color_list())
    return html
