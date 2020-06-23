from Product import Product
from ChassisDJI import ChassisDJI
from PropellerDJI import PropellerDJI
from CameraDJI import CameraDJI


class DJI(Product):

    def chassis(self):
        super().chassis()
        c = ChassisDJI()
        return c.createChassis()

    def camera(self):
        super().camera()
        c = CameraDJI()
        return c.createCamera()

    def propeller(self):
        super().propeller()
        p = PropellerDJI()
        return p.createPropeller()
