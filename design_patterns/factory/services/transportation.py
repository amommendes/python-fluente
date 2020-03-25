from abc import ABC, abstractmethod

class Transportation(ABC):
    """
    This interface declare common operation to product subclasses 
    """

    @abstractmethod
    def delivery(self) -> str:
        """Delivery method should be implemented to transportation subclass 
        
        :return: return the delivery operation
        :rtype: str
        """
        pass


class Truck(Transportation):
    """This is the product that implements common methods from Transportation interface
    """    
    def delivery(self) -> str:
        return("Hey, your package will delivered by a big Truck!")
