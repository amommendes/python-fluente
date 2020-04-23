from design_patterns.builder.builder import GenericBuilder

class CarDirector:
    def __init__(self):
        self.__builder = None

    @property
    def builder(self):
        return self.__builder

    @builder.setter
    def builder(self, builder: GenericBuilder) -> None:
        self.__builder = builder

    def makeSUV(self):
        self.builder.setSeats(6)
        self.builder.setEngine("Automatic")
        self.builder.setGPS(True)
        self.builder.setTripComputer(True)

    def makeSportCar(self):
        self.builder.setSeats(2)
        self.builder.setEngine("Manual")
        self.builder.setGPS(True)
        self.builder.setTripComputer(True)
