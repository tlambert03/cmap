try:
    import colorcet as _cc
except ModuleNotFoundError as e:
    raise ModuleNotFoundError("must install colorcet to use colorcet palettes") from e

__license__ = "CC-BY-4.0"
__source__ = "https://github.com/holoviz/colorcet"


def __dir__() -> list[str]:
    return _cc.all_original_names()  # type: ignore


def __getattr__(name: str) -> list[list[float]]:
    data = getattr(_cc, name)
    if not isinstance(data, list):
        raise ValueError(f"Invalid colormap name: {name}")
    return data
