class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year
    
    @property
    def brand(self):
        return self._brand
    
    @property
    def year(self):
        return self._year
    
    def get_info(self):
        print(f"Vehicle's brand: {self._brand}")
        print(f"Vehicle's year: {self._year}")

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors
    
    def get_info(self):
        print(f"Car's brand is: {self.brand}")
        print(f"Car's year is: {self.year}")
        print(f"This car has {self.doors} doors")

class Motorcycle(Vehicle):
    def __init__(self, brand, year, motorcycle_type):
        super().__init__(brand, year)
        self.type = motorcycle_type
    
    def get_info(self):
        print(f"Motorcycle's brand is: {self.brand}")
        print(f"Motorcycle's year is: {self.year}")
        print(f"This motorcycle is {self.type} style")

vehicle1 = Car("Toyota", 2020, 4)
vehicle2 = Motorcycle("Yamaha", 2022, "Sports")

vehicle1.get_info()
vehicle2.get_info()