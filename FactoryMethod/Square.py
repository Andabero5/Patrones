from Shape import Shape


class Square(Shape):
    @classmethod
    def draw(cls):
        super().draw()
        return "Drew Square"
