from pathlib import Path

import mkdocs_gen_files
from cmap._catalog import CATALOG

DOCS = Path(__file__).parent
TEMPLATE = """# {name}

{{{{ cmap_linearity: {name} }}}}
"""

for name, info in CATALOG.items():
    try:
        category = info["category"]
        with mkdocs_gen_files.open(f"cmaps/{category}/{name}.md", "w") as f:
            f.write(TEMPLATE.format(name=name))
    except Exception:
        breakpoint()
    # mkdocs_gen_files.set_edit_path(filename, "gen_pages.py")
