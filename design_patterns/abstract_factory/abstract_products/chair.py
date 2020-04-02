from abc import ABC,abstractmethod


class Chair(ABC):
    
    @abstractmethod
    def color():
        pass

    @abstractmethod
    def has_gold(self):
        pass
    
    @abstractmethod
    def size(self):
        pass


