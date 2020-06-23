from Camera import Camera


class CameraDJI(Camera):
    def createCamera(self):
        super().createCamera()
        return "Camara de DJI"
