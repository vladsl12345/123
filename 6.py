class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        print(f"{self.year} {self.make} {self.model}")


my_car = Car("Ford", "Mustang", 2021)
second_car = Car("Toyota", "Camry", 2022)

my_car.get_info()
second_car.get_info()