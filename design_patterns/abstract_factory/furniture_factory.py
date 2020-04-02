from abc import ABC,abstractmethod
from design_patterns.abstract_factory.abstract_products.chair import Chair
from design_patterns.abstract_factory.abstract_products.coffe_table import CoffeTable



class FurnitureAbstractFactory(ABC):
    
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_coffe_table(self) -> CoffeTable:
        pass


