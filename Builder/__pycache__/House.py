class House():
    def __init__(self):
        self.__door = ""
        self.__pool = ""
        self.__window = ""
        self.__wall = ""

    def setDoor(self, door):
        self.__door = door

    def setPool(self, pool):
        self.__pool = pool

    def setWindow(self, window):
        self.__window = window

    def setWall(self, wall):
        self.__wall = wall

    def getDoor(self):
        return self.__door

    def getPool(self):
        return self.__pool

    def getWindow(self):
        return self.__window

    def getWall(self):
        return self.__wall
