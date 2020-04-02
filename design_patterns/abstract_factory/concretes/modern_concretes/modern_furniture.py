from design_patterns.abstract_factory.furniture_factory import FurnitureAbstractFactory
from design_patterns.abstract_factory.abstract_products.chair import Chair
from design_patterns.abstract_factory.abstract_products.coffe_table import CoffeTable

class ModernChair(Chair):
    
    @staticmethod
    def color():
        return "ocean blue" 

    @staticmethod
    def has_gold():
        return False
    
    @staticmethod
    def size():
        return 5

class ModernCoffeTable(CoffeTable):

    @staticmethod
    def size():
        return 15

    @staticmethod
    def color():
        return "ocean blue"

class ModernFurniture(FurnitureAbstractFactory):

    def create_chair(self) -> ModernChair:
        return ModernChair
    
    def create_coffe_table(self) -> ModernCoffeTable:
        return ModernCoffeTable


