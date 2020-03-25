from abc import ABC, abstractmethod
from design_patterns.factory.services.transportation import Truck

class TransportationCreator(ABC):
    """
        This is the abstract creator
        :return: returns the desired transportation method
    """

    @abstractmethod
    def create_transport(self):
        pass


class TruckCreator(TransportationCreator):
    """ This creator implement create_tranport abstract method 
    """    
    def create_transport(self)-> Truck:
        return Truck()