from BlackDog import BlackDog
from WhiteDog import WhiteDog


class DogFactory():

    @classmethod
    def createDog(cls, option, number):
        if option == 1:
            dog = WhiteDog(number)
            return dog._type+str(dog._value)
        else:
            dog = BlackDog(number)
            return dog._type+str(dog._value)
