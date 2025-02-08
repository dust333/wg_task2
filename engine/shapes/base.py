import tkinter as tk
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(
        self,
        x: int,
        y: int,
    ):
        self.x: int = x
        self.y: int = y
        self.color: str = ""

    @abstractmethod
    def draw(self, canvas: tk.Canvas) -> None:
        pass
