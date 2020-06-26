import copy
from BlackDog import BlackDog
from WhiteDog import WhiteDog
from DogFactory import DogFactory
from Prototype import Prototype


def main():
    listDog = []
    while True:
        dog = int(
            input("Que perro desea generar\n1. perro blanco\n2. Perro negro\n"))
        if dog == 1 or 2:
            while True:
                number = int(
                    input("¿Cuantos perros desea generar?\nEl valor no debe superar 10\n"))
                if number != range(1, 10):
                    for i in range(0, number):
                        listDog.append(DogFactory.createDog(dog, i+1))
                    print(listDog)
                    break
                else:
                    print("escriba un valor valido")
            break
        else:
            print("escriba un valor valido")


if __name__ == "__main__":
    main()
