from unittest.mock import patch

import pytest

from engine.shapes.circle import Circle
from engine.shapes.rectangle import Rectangle
from engine.shapes.triangle import Triangle


@pytest.mark.shape
class TestShapes:
    @pytest.mark.parametrize(
        "shape, method, args",
        (
            (
                triangle := Triangle(10, 20, 20),
                "create_polygon",
                (triangle.points,),
            ),
            (
                rectangle := Rectangle(10, 20, 30, 40),
                "create_rectangle",
                (
                    rectangle.x,
                    rectangle.y,
                    rectangle.width + rectangle.x,
                    rectangle.height + rectangle.y,
                ),
            ),
            (
                circle := Circle(10, 20, 30),
                "create_oval",
                (
                    circle.x - circle.radius,
                    circle.y - circle.radius,
                    circle.x + circle.radius,
                    circle.y + circle.radius,
                ),
            ),
        ),
    )
    def test_shape_draw(self, canvas_mock, shape, method, args) -> None:
        shape.draw(canvas_mock)
        getattr(canvas_mock, method).assert_called_once_with(
            *args, outline=shape.color, fill=shape.color
        )

    @pytest.mark.parametrize(
        "shape, text",
        (
            (
                triangle := Triangle(10, 20, 20),
                f"Drawing {triangle.color} {triangle.__class__.__name__}: "
                f"({triangle.x}, {triangle.y}) with points {tuple(triangle.points)}",
            ),
            (
                rectangle := Rectangle(10, 20, 30, 40),
                f"Drawing {rectangle.color} {rectangle.__class__.__name__}: "
                f"({rectangle.x}, {rectangle.y}) with width {rectangle.width}, height {rectangle.height}",
            ),
            (
                circle := Circle(10, 20, 30),
                f"Drawing {circle.color} {circle.__class__.__name__}: "
                f"({circle.x}, {circle.y}) with radius {circle.radius}",
            ),
        ),
    )
    def test_shape_print(self, canvas_mock, shape, text) -> None:
        with patch("builtins.print") as mock_print:
            shape.draw(canvas_mock)
            mock_print.assert_called_once_with(text)

    @pytest.mark.parametrize(
        "shape_class, init_data, assert_data",
        (
            (
                Triangle,
                (x := 10, y := 20, size := 30),
                {
                    "x": x,
                    "y": y,
                    "points": [
                        x - size,
                        y - size,
                        x + size,
                        y + size,
                        x + size,
                        y - size,
                    ],
                    "color": "",
                },
            ),
            (
                Rectangle,
                (x := 10, y := 20, width := 30, height := 40),
                {
                    "x": x,
                    "y": y,
                    "width": width,
                    "height": height,
                    "color": "",
                },
            ),
            (
                Circle,
                (x := 10, y := 20, radius := 30),
                {
                    "x": x,
                    "y": y,
                    "radius": radius,
                    "color": "",
                },
            ),
        ),
    )
    def test_shape_init(self, shape_class, init_data, assert_data) -> None:
        shape = shape_class(*init_data)

        for arg, value in assert_data.items():
            assert getattr(shape, arg) == value
