class cardata:
    def __init__(car, brand, maker, year, models):
      car.brand = brand
      car.maker = maker
      car.year = year
      car.models = models

newcar = cardata("benz", "germany", "2024", "glk")
print(newcar.year)