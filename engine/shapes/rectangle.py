import tkinter as tk

from engine.shapes.base import Shape


class Rectangle(Shape):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def draw(self, canvas: tk.Canvas) -> None:
        print(
            f"Drawing {self.color} {self.__class__.__name__}: ({self.x}, {self.y}) with width {self.width}, height {self.height}"
        )
        canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.width,
            self.y + self.height,
            outline=self.color,
            fill=self.color,
        )
