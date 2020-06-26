from Shape import Shape


class Circle(Shape):
    @classmethod
    def draw(cls):
        super().draw()
        return "Drew Circle"
