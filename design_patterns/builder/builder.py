from abc import ABC, abstractmethod

class GenericBuilder(ABC):
    """A car is a complex object that can be constructed in a hundred different ways. Instead of bloating the Car class
        with a huge constructor, we extracted the car assembly code into a separate car builder class.
        This class has a set of methods for configuring various parts of a car.
    """
    @property
    @abstractmethod
    def product(self) -> None:
        """
        This method returns the product itself, in our case it can return a Car or a Manual's car
        :return: new Product
        """
        pass

    @abstractmethod
    def setSeats(self, number) -> None:
        pass

    @abstractmethod
    def setEngine(self, engine) -> None:
        pass

    @abstractmethod
    def setTripComputer(self) -> None:
        pass

    @abstractmethod
    def setGPS(self) -> None:
        pass
