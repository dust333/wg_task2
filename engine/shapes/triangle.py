import tkinter as tk

from engine.shapes.base import Shape


class Triangle(Shape):
    def __init__(self, x: int, y: int, size: int):
        super().__init__(x, y)
        self.points = [x - size, y - size, x + size, y + size, x + size, y - size]

    def draw(self, canvas: tk.Canvas) -> None:
        print(
            f"Drawing {self.color} {self.__class__.__name__}: ({self.x}, {self.y}) with points {tuple(self.points)}"
        )
        canvas.create_polygon(self.points, outline=self.color, fill=self.color)
