class Car:
    def __init__(self, max_speed, color, model):
        self.max_speed = max_speed
        self.color = color
        self.model = model
        self.__fined = False

    def pay_fine(self):
        # сеттер
        if self.__fined:
            self.__fined = False

    def get_fined(self):
        # геттер
        return self.__fined

    def drive_to_location(self, location):
        if self.__fined:
            raise ValueError(f"Car {self.model} is fined and can not drive anywhere.")
        print(f"Car {self.model} is driving to {location}")

    def __test(self):
        print("Private method")

    @property
    def fined(self):
        # getter
        return self.__fined

    @fined.settergit
    def fined(self, value):
        # setter
        self.__fined = value

class Truck(Car):
    def test(self):
        print(f"Truck test {self.get_fined()}")

car_honda = Car(140, "silver", "Honda Fit")
car_honda.drive_to_location("Karakol")
print(car_honda.get_fined())
print(car_honda.fined)
car_honda.fined = True
# car_honda.drive_to_location("Karakol")
truck_man = Truck(200, "grey", "MAN")
truck_man.test()
print(car_honda._Car__fined)