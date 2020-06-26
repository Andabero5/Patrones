from Shape import Shape
from Square import Square
from Circle import Circle
from Rectangle import Rectangle


class ShapeFactory():
    @classmethod
    def getShape(cls, option):
        if option == 1:
            return Circle.draw()
        elif option == 2:
            return Square.draw()
        elif option == 3:
            return Rectangle.draw()
