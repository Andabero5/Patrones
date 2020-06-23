from Chassis import Chassis


class ChassisDJI(Chassis):
    def createChassis(self):
        super().createChassis()
        return "Chasis de DJI"
