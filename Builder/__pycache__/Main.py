from Mansion import *
from Director import *


class main():
    mansion = Mansion()
    director = Director()
    director.setBuilder(mansion)
    house = director.getHouse()
    print(f"{house.getDoor()}\n{house.getPool()}\n{house.getWindow()}\n{house.getWall()}")


if __name__ == main:
    main()
