from design_patterns.abstract_factory.furniture_factory import FurnitureAbstractFactory
from design_patterns.abstract_factory.abstract_products.chair import Chair
from design_patterns.abstract_factory.abstract_products.coffe_table import CoffeTable

class VictorianChair(Chair):
    """
        This a concrete product from Chair abstract product
    """
    @staticmethod
    def color():
        return "red"

    @staticmethod
    def has_gold():
        return True

    @staticmethod
    def size():
        return 10

class VictorianCoffeTable(CoffeTable):
    """
        This a concrete product from CoffeTable abstract product
    """
    @staticmethod
    def size():
        return 25

    @staticmethod
    def color():
        return "timber"

class VictorianFurniture(FurnitureAbstractFactory):

    def create_chair(self) -> VictorianChair:
        return VictorianChair
    
    def create_coffe_table(self) -> VictorianCoffeTable:
        return VictorianCoffeTable


