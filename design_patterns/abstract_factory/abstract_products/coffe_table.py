from abc import ABC,abstractmethod


class CoffeTable(ABC):
    
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def color(self):
        pass


