from design_patterns.builder.car.car_builder import CarBuilder
from design_patterns.builder.car_director.director import CarDirector

colors = {"red": "\033[1;1;31m", "blue_background": "\033[1;0;46m", "bold": "\033[1;0;1m", "normal": "\033[1;40;0m" }


if __name__ == "__main__":
    director = CarDirector()
    builder = CarBuilder()
    director.builder = builder

    print(f"""{colors["blue_background"]}SUV car {colors["normal"]}""")
    director.makeSUV()
    builder.product.describe()
    print(f"""{colors["blue_background"]} Sport Car {colors["normal"]}""")
    director.makeSportCar()
    builder.product.describe()
