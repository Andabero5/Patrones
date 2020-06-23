from Builder import *


class Mansion(Builder):
    def buildDoor(self):
        super().buildDoor()
        return "20 doors"

    def buildPool(self):
        super().buildPool()
        return "1 pool"

    def buildWindow(self):
        super().buildWindow()
        return "20 windows"

    def buildWall(self):
        super().buildWall()
        return "80 walls"
