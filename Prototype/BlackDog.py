import copy
from Prototype import Prototype


class BlackDog(Prototype):
    """ Concrete prototype. """

    def __init__(self, number):
        self._type = "BlackDog"
        self._value = number

    def clone(self):
        super().clone()
        return copy.copy(self)
