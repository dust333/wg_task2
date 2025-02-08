import tkinter as tk

from engine.shapes.base import Shape


class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y)
        self.radius = radius

    def draw(self, canvas: tk.Canvas) -> None:
        print(
            f"Drawing {self.color} {self.__class__.__name__}: ({self.x}, {self.y}) with radius {self.radius}"
        )
        canvas.create_oval(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
            outline=self.color,
            fill=self.color,
        )
