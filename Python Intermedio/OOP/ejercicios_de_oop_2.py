class Bus:
    
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers_on_board = []
    
    def add_passenger(self, name):
        if len(self.passengers_on_board) == self.max_passengers:
            print(f"Full bus! No room for {name} in this bus!")
        else:
            self.passengers_on_board.append(name)
    
    def show_details(self, type):
        print(f"{type} capacity is {self.max_passengers} and it carries {len(self.passengers_on_board)} passengers")
        for passenger in self.passengers_on_board:
            print(passenger)

class Person:
    def __init__(self, name):
        self.name = name
        self.age = 0

small_bus = Bus(2)
big_bus = Bus(20)
person_1 = Person("Kurt")
person_2 = Person("Mia")
person_3 = Person("Sophie")
person_4 = Person("David")

small_bus.add_passenger(person_1.name)
small_bus.add_passenger(person_2.name)
if len(small_bus.passengers_on_board) == small_bus.max_passengers:
    big_bus.add_passenger(person_3.name)
else:
    small_bus.add_passenger(person_3.name)
small_bus.add_passenger(person_4.name)

small_bus.show_details('Small bus')
big_bus.show_details('Big bus')