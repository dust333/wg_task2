from engine.core.engine2d import Engine2D
from engine.shapes.circle import Circle
from engine.shapes.rectangle import Rectangle
from engine.shapes.triangle import Triangle


def main():
    engine = Engine2D()

    engine.set_color("red")
    engine.add_shape(Circle(100, 100, 50))
    engine.set_color("blue")
    engine.add_shape(Rectangle(200, 50, 150, 100))
    engine.add_shape(Triangle(300, 300, 70))
    engine.draw()


if __name__ == "__main__":
    main()
