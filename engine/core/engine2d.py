import tkinter as tk
from typing import List

from engine.shapes.base import Shape


class Engine2D:
    def __init__(self, width: int = 600, height: int = 400, clear_time: int = 3000):
        self._clear_time = clear_time
        self._window = tk.Tk()
        self._canvas = tk.Canvas(self._window, width=width, height=height, bg="white")
        self._canvas.pack()
        self._current_color = "black"
        self._shapes_to_draw: List[Shape] = []

    @property
    def current_color(self) -> str:
        return self._current_color

    def set_color(self, color: str) -> None:
        if isinstance(color, str):
            self._current_color = color
        else:
            raise TypeError("Color must be a str")

    def add_shape(self, shape: Shape) -> None:
        if isinstance(shape, Shape):
            shape.color = self._current_color
            self._shapes_to_draw.append(shape)
        else:
            raise TypeError("Shape must be instance of Shape")

    def get_shapes(self) -> List[Shape]:
        return self._shapes_to_draw

    def draw(self) -> None:  # назвал как задании, хотя так назвал бы его draw_and_clear
        for shape in self._shapes_to_draw:
            shape.draw(self._canvas)
        self._shapes_to_draw = []

        self._window.after(3000, self.clear_canvas)
        self._window.mainloop()

    def clear_canvas(self) -> None:
        self._canvas.delete("all")
