from design_patterns.builder.builder import GenericBuilder

class Car:

    def __init__(self):
        self.seats = None
        self.engine = None
        self.trip_computer = None
        self.gps = None

    def describe(self):
        print(f"Seats: {self.seats}\nEngine: {self.engine}\n"
              f"Has Trip Computer: {self.trip_computer}\nHas GPS: {self.gps}")


class CarBuilder(GenericBuilder):

    def __init__(self):
        self.car = None
        self.reset()

    @property
    def product(self) -> Car:
        car = self.car
        self.reset()
        return car

    def reset(self) -> None:
        self.car = Car()

    def setSeats(self, number) -> None:
        self.car.seats = number


    def setEngine(self, engine):
        self.car.engine = engine

    def setGPS(self, has_gps) -> None:
        self.car.gps = has_gps

    def setTripComputer(self, has_trip_computer) -> None:
        self.car.trip_computer = has_trip_computer


class Manual():

    def __init__(self):
        self.seats = None
        self.engine = None
        self.trip_computer = None
        self.gps = None

    def describe(self):
        print(f"""This your manual. Please read carefully.\n""" +
        f"""Seats: {self.seats}\nEngine: {self.engine}\nHas Trip Computer: {self.trip_computer}\nHas GPS: {self.gps}""")

class ManualBuilder(GenericBuilder):
    def __init__(self):
        self.car = None
        self.reset()

    @property
    def product(self) -> Manual:
        car = self.car
        self.reset()
        return car

    def reset(self) -> None:
        self.car = Manual()

    def setSeats(self, number) -> None:
        self.car.seats = number


    def setEngine(self, engine):
        self.car.engine = engine

    def setGPS(self, has_gps) -> None:
        self.car.gps = has_gps

    def setTripComputer(self, has_trip_computer) -> None:
        self.car.trip_computer = has_trip_computer

