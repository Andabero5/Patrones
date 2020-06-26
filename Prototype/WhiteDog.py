import copy
from Prototype import Prototype


class WhiteDog(Prototype):

    def __init__(self, number):
        self._type = "WhiteDog"
        self._value = number

    def clone(self):
        super().clone()
        return copy.copy(self)
