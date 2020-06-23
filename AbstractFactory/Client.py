from DJI import *
from Hubsand import *


class Client():

    def __init__(self):
        self.droneList = [DJI(), Hubsand()]

    def chooseDrone(self):
        drone = int(
            input("¿Qué marca de drone desea?\nMarque 1 para DJI\nMarque 2 para Hubsand\n"))
        if drone == 1:
            brandDrone = self.droneList[0]
        elif drone == 2:
            brandDrone = self.droneList[1]

        camera = brandDrone.camera()
        chassis = brandDrone.chassis()
        propeller = brandDrone.propeller()

        return f"se ha creado {camera}, {chassis}, {propeller}"
