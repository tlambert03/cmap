import os
import sys
from typing import TYPE_CHECKING
from unittest.mock import MagicMock, patch

import numpy as np
import pytest
from cmap import Color, Colormap

if TYPE_CHECKING:
    from qtpy.QtWidgets import QApplication

CMAP = Colormap(["black", (0, 1, 0), "00FFFF33", "w"])
IMG = np.random.rand(10, 10).astype("float32")


def test_pydantic_support() -> None:
    pydantic = pytest.importorskip("pydantic.color")

    assert Color(pydantic.Color("red")) is Color("red")


def test_colour_support() -> None:
    colour = pytest.importorskip("colour")
    assert Color(colour.Color("red")) is Color("red")


def test_rich_repr() -> None:
    rich = pytest.importorskip("rich")
    from rich.text import Text

    mock = MagicMock()
    with patch.object(rich, "get_console", lambda: mock):
        Color("red").__rich_repr__()
    mock.print.assert_called_once_with(Text("  ", style="on red"), end="")


def test_matplotlib() -> None:
    plt = pytest.importorskip("matplotlib.pyplot")
    plt.imshow(IMG, cmap=CMAP.to_mpl())


@pytest.mark.skipif(sys.version_info >= (3, 11), reason="napari not working on py3.11")
def test_napari(qapp: "QApplication") -> None:
    napari = pytest.importorskip("napari")

    napari.view_image(IMG, colormap=CMAP.to_napari())


def test_vispy(qapp: "QApplication") -> None:
    scene = pytest.importorskip("vispy.scene")

    canvas = scene.SceneCanvas(keys="interactive")
    canvas.size = 800, 600
    canvas.show()
    view = canvas.central_widget.add_view()
    view.camera = scene.PanZoomCamera(aspect=1)
    scene.visuals.Image(IMG, cmap=CMAP.to_vispy(), parent=view.scene)
    view.camera.flip = (0, 1, 0)
    view.camera.set_range()


@pytest.mark.skipif(os.name == "nt" and sys.version_info >= (3, 11), reason="segfaults")
def test_plotly() -> None:
    px = pytest.importorskip("plotly.express")

    px.imshow(IMG, color_continuous_scale=CMAP.to_plotly())


@pytest.mark.skip(reason="segfaults")
def test_pygfx(qapp) -> None:
    gfx = pytest.importorskip("pygfx")
    auto = pytest.importorskip("wgpu.gui.auto")

    canvas = auto.WgpuCanvas(size=IMG.shape)
    renderer = gfx.renderers.WgpuRenderer(canvas)
    camera = gfx.OrthographicCamera(*IMG.shape)
    camera.position.y = IMG.shape[0] / 2
    camera.position.x = IMG.shape[1] / 2
    camera.scale.y = -1

    scene = gfx.Scene()
    scene.add(
        gfx.Image(
            gfx.Geometry(grid=gfx.Texture(IMG, dim=2)),
            gfx.ImageBasicMaterial(clim=(0, IMG.max()), map=CMAP.to_pygfx()),
        )
    )

    def animate() -> None:
        renderer.render(scene, camera)
        canvas.request_draw()

    canvas.request_draw(animate)


def test_bokeh() -> None:
    from bokeh.plotting import figure

    p = figure()
    h, w = IMG.shape
    p.image(image=[np.flipud(IMG)], x=0, y=0, dw=w, dh=h, color_mapper=CMAP.to_bokeh())


# def microvis_imshow(img_data: np.ndarray, cmap: cmap.Colormap) -> None:
#     from microvis import _util, imshow

#     with _util.exec_if_new_qt_app():
#         imshow(img_data, cmap=cmap)


# def altair_chart(cmap: cmap.Colormap) -> None:
#     # altair doesn't do images well... using random data
#     import altair as alt
#     import pandas as pd

#     alt.renderers.enable("altair_viewer")

#     values = np.random.randn(100).cumsum()
#     data = pd.DataFrame(
#         {"value": values},
#         index=pd.date_range("2018", freq="D", periods=100),
#     )
#     chart = (
#         alt.Chart(data.reset_index())
#         .mark_circle()
#         .encode(
#             x="index:T",
#             y="value:Q",
#             color=alt.Color(
#                 "value",
#                 scale=alt.Scale(
#                     domain=(values.min(), values.max()),
#                     # this is the important part
#                     range=cmap.to_altair(),
#                 ),
#             ),
#         )
#     )
#     chart.show()
