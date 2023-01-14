from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING, Iterator, Literal, Mapping, cast

import cmap.data

if TYPE_CHECKING:
    from typing_extensions import NotRequired, TypeAlias, TypedDict

    from ._colormap import ColorStopsLike

    Category: TypeAlias = Literal[
        "sequential", "diverging", "cyclic", "qualitative", "miscellaneous"
    ]

    class CatalogItem(TypedDict):
        data: str
        category: Category
        tags: NotRequired[list[str]]
        interpolation: NotRequired[bool]
        info: NotRequired[str]

    # would be nice to subclass CatalogItem... but can't
    # https://github.com/python/mypy/issues/7435
    class LoadedCatalogItem(TypedDict):
        data: ColorStopsLike
        tags: list[str]
        category: Category
        interpolation: NotRequired[bool]
        license: str
        source: str
        info: str

    CatalogDict: TypeAlias = dict[str, CatalogItem]


def _norm_name(name: str) -> str:
    return name.lower().replace(" ", "_")


CATALOG: dict[str, CatalogItem] = {}

for r in Path(cmap.data.__file__).parent.rglob("record.json"):
    with open(r) as f:
        data = json.load(f)
        for k, v in data["colormaps"].items():
            v.setdefault("license", data["license"])
            v.setdefault("namespace", data["namespace"])
            v.setdefault("source", data["source"])
            v.setdefault("authors", data["authors"])
            if "category" in data:
                v.setdefault("category", data["category"])
            CATALOG[k] = v

_CATALOG_LOWER = {_norm_name(k): v for k, v in CATALOG.items()}


class Catalog(Mapping[str, "LoadedCatalogItem"]):

    _loaded: dict[str, LoadedCatalogItem] = {}

    def __iter__(self) -> Iterator[str]:
        return iter(CATALOG)

    def __len__(self) -> int:
        return len(CATALOG)

    def __getitem__(self, name: str) -> LoadedCatalogItem:
        if name not in self._loaded:
            if (key := _norm_name(name)) not in _CATALOG_LOWER:
                # TODO: print a list of available colormaps or something
                if name != key:
                    raise ValueError(f"Colormap {name!r} (or {key!r}) not found.")
                raise ValueError(f"Colormap {name!r} not found.")

            self._loaded[name] = self._load(key)
            if key != name:
                # cache the requested name as well so we don't need to renormalize
                self._loaded[key] = self._loaded[name]
        return self._loaded[name]

    def _load(self, key: str) -> LoadedCatalogItem:
        """Get the data for a named colormap."""
        item = _CATALOG_LOWER[key].copy()
        _item = cast("LoadedCatalogItem", item)
        if isinstance(_item["data"], str):
            module, attr = item["data"].rsplit(":", 1)
            # not encouraged... but significantly faster than importlib
            # well tested on internal data though
            mod = __import__(module, fromlist=[attr])
            _item["data"] = getattr(mod, attr)
        _item.setdefault("tags", [])
        _item.setdefault("info", "")
        return _item


catalog = Catalog()
