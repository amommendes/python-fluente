from design_patterns.abstract_factory.furniture_factory import FurnitureAbstractFactory
from design_patterns.abstract_factory.concretes.modern_concretes.modern_furniture import ModernFurniture
from design_patterns.abstract_factory.concretes.victorian_concretes.victorian_furniture import VictorianFurniture

colors = {"red": "\033[1;1;31m", "blue_background": "\033[1;0;46m", "bold": "\033[1;0;1m", "normal": "\033[1;40;0m" }

def client_code(factory: FurnitureAbstractFactory):
    chair = factory.create_chair()
    coffe_table = factory.create_coffe_table()

    print(f"""{colors["blue_background"]}Chair Characteristcs{colors["normal"]}
        {colors["bold"]}Chair Type{colors["normal"]}: {type(factory).__name__},
        {colors["bold"]}Chair color{colors["normal"]}: {chair.color()},
        {colors["bold"]}Chair has gold{colors["normal"]}: {chair.has_gold()}
        {colors["bold"]}Chair size{colors["normal"]}: {chair.size()}
    """)
    print(f"""{colors["blue_background"]}CoffeTable Characteristcs{colors["normal"]}
        {colors["bold"]}CoffeTable Type{colors["normal"]}: {type(factory).__name__},
        {colors["bold"]}CoffeTable color{colors["normal"]}: {coffe_table.color()},
        {colors["bold"]}CoffeTable size{colors["normal"]}: {coffe_table.size()}
    """)


if __name__ == "__main__":
    print(f"{colors['red']}Modern Furniture ")
    client_code(ModernFurniture())
    print(f"{colors['red']}Victorian Furniture ")
    client_code(VictorianFurniture())
