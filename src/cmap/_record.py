from typing import Literal, Sequence

Category = Literal["sequential", "diverging", "cyclic", "qualitative", "miscellaneous"]


class ColormapRecord_mypy:
    __slots__ = ("data", "category", "tags", "interpolation", "info")

    def __init__(
        self,
        data: str,
        category: Category,
        tags: Sequence[str] = (),
        interpolation: bool = True,
        info: str = "",
    ):
        self.data = data
        self.category = category
        self.tags = tags
        self.interpolation = interpolation
        self.info = info
