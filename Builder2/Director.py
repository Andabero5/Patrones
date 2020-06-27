from House import *


class Director():
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getHouse(self):
        house = House()
        house.setDoor(self.__builder.buildDoor())
        house.setPool(self.__builder.buildPool())
        house.setWindow(self.__builder.buildWindow())
        house.setWall(self.__builder.buildWall())
        return house
