import tkinter
from unittest.mock import Mock

import pytest

from engine.core.engine2d import Engine2D
from engine.shapes.circle import Circle
from engine.shapes.rectangle import Rectangle
from engine.shapes.triangle import Triangle

shape_mocks = (
    Mock(spec=Rectangle),
    Mock(spec=Triangle),
    Mock(spec=Circle),
)


@pytest.fixture
def engine() -> Engine2D:
    return Engine2D(width=800, height=600)


@pytest.fixture
def engine_with_shape_mocks() -> Engine2D:
    engine = Engine2D(width=800, height=600)
    for shape in shape_mocks:
        engine.add_shape(shape)

    return engine


@pytest.fixture
def canvas_mock() -> Mock:
    return Mock(spec=tkinter.Canvas)
