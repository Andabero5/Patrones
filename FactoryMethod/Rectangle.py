from Shape import Shape


class Rectangle(Shape):
    @classmethod
    def draw(cls):
        super().draw()
        return "Drew Rectangle"
