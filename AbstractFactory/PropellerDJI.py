from Propeller import Propeller


class PropellerDJI(Propeller):
    def createPropeller(self):
        super().createPropeller()
        return "Helices de DJI"
