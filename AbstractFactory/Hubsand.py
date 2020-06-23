from Product import Product
from ChassisHubsand import ChassisHubsand
from PropellerHubsand import PropellerHubsand
from CameraHubsand import CameraHubsand


class Hubsand (Product):
    def chassis(self):
        super().chassis()
        h = ChassisHubsand()
        return h.createChassis()

    def camera(self):
        super().camera()
        h = CameraHubsand()
        return h.createCamera()

    def propeller(self):
        super().propeller()
        h = PropellerHubsand()
        return h.createPropeller()
