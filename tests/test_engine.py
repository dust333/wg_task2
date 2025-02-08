import tkinter as tk
from unittest.mock import patch

import pytest

from engine.core.engine2d import Engine2D
from tests.conftest import shape_mocks


@pytest.mark.engine
@pytest.mark.engine_init
class TestEngineInitialization:
    def test_initial_state(self) -> None:
        with patch.object(tk.Canvas, "pack") as mock_pack:
            engine = Engine2D(width=800, height=600, clear_time=3000)
            mock_pack.assert_called_once()

            assert engine._shapes_to_draw == []
            assert engine._current_color == "black"
            assert engine._clear_time == 3000
            assert isinstance(engine._canvas, tk.Canvas)
            assert isinstance(engine._window, tk.Tk)
            assert isinstance(engine._shapes_to_draw, list)

    def test_initial_state_canvas(self) -> None:
        with patch.object(tk, "Canvas") as mock_pack:
            engine = Engine2D(width=800, height=600, clear_time=3000)
            mock_pack.assert_called_once_with(
                engine._window, width=800, height=600, bg="white"
            )


@pytest.mark.engine
@pytest.mark.engine_color
class TestEngineColor:
    def test_set_color(self, engine) -> None:
        engine.set_color("red")
        assert engine.current_color == "red"

    def test_set_multiple_colors_to_multiple_shapes(self, engine) -> None:
        engine.set_color(first_color := "black")
        engine.add_shape(shape_mocks[0])

        engine.set_color(second_color := "yellow")
        engine.add_shape(shape_mocks[1])

        assert shape_mocks[0].color == first_color
        assert shape_mocks[1].color == second_color

    def test_set_color_multiple_times(self, engine) -> None:
        engine.set_color("red")
        assert engine.current_color == "red"

        engine.set_color("blue")
        assert engine.current_color == "blue"

        engine.set_color("green")
        assert engine.current_color == "green"

    def test_get_current_color(self, engine) -> None:
        assert engine.current_color == "black"

    def test_set_color_invalid_type(self, engine) -> None:
        with pytest.raises(TypeError, match="Color must be a str"):
            engine.set_color(123)  # noqa


@pytest.mark.engine
@pytest.mark.engine_shape
class TestEngineShapes:
    @pytest.mark.parametrize("shape", shape_mocks)
    def test_add_shape(self, engine, shape) -> None:
        initial_shape_count = len(engine.get_shapes())
        engine.add_shape(shape)
        assert len(engine.get_shapes()) == initial_shape_count + 1
        assert shape.color == engine.current_color

    def test_add_shapes(self, engine) -> None:
        for shape in shape_mocks:
            engine.add_shape(shape)
            assert shape.color == engine.current_color
        assert list(shape_mocks) == engine.get_shapes()

    def test_get_shapes(self, engine, engine_with_shape_mocks) -> None:
        assert engine.get_shapes() == []
        assert engine_with_shape_mocks.get_shapes() == list(shape_mocks)

    @pytest.mark.parametrize("shape", shape_mocks)
    def test_add_same_shape_twice(self, engine, shape) -> None:
        engine.add_shape(shape)
        engine.add_shape(shape)

        assert len(engine.get_shapes()) == 2

    def test_add_shape_incorrect_type(self, engine) -> None:
        with pytest.raises(TypeError, match="Shape must be instance of Shape"):
            engine.add_shape("string")  # noqa


@pytest.mark.engine
@pytest.mark.engine_draw
class TestEngineDrawing:
    @pytest.mark.parametrize("shape", shape_mocks)
    def test_draw_shape(self, engine, shape) -> None:
        engine.add_shape(shape)

        with (
            patch.object(engine._window, "mainloop"),
            patch.object(engine._window, "after") as mock_after,
            patch.object(shape, "draw") as mock_draw,
        ):
            engine.draw()

            mock_draw.assert_called_once_with(engine._canvas)
            mock_after.assert_called_once_with(engine._clear_time, engine.clear_canvas)

    def test_draw_multiple_shapes(self, engine) -> None:
        for shape in shape_mocks:
            engine.add_shape(shape)

        with (
            patch.object(engine._window, "mainloop"),
            patch.object(shape_mocks[0], "draw") as mock_draw_1,
            patch.object(shape_mocks[1], "draw") as mock_draw_2,
            patch.object(shape_mocks[2], "draw") as mock_draw_3,
            patch.object(engine._window, "after") as mock_after,
        ):
            engine.draw()
            mock_draw_1.assert_called_once_with(engine._canvas)
            mock_draw_2.assert_called_once_with(engine._canvas)
            mock_draw_3.assert_called_once_with(engine._canvas)

            mock_after.assert_called_once_with(engine._clear_time, engine.clear_canvas)


@pytest.mark.engine
@pytest.mark.engine_clear
class TestEngineClearCanvas:
    def test_clear_canvas(self, engine) -> None:
        with patch.object(tk.Canvas, "delete") as mock_delete:
            engine.clear_canvas()
            mock_delete.assert_called_once_with("all")
