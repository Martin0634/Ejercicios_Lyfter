import random

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers_on_board = []
    
    def passenger_waiting(self, name):
        print(f"{name} is waiting at the bus stop.")
        print(f"{name} wants to get into the bus.")
    
    def add_passenger(self, name):
        if len(self.passengers_on_board) >= self.max_passengers:
            print(f"Full bus! No room for {name} in this bus!")
        else:
            self.passengers_on_board.append(name)
            print(f"{name} is in the bus.")
            
    def remove_passenger(self):
        passenger = random.randint(0, (len(self.passengers_on_board)-1))
        print(f"{self.passengers_on_board[passenger]} got off the bus.")
        self.passengers_on_board.pop(passenger)
        
    
    def show_details(self):
        print(f"Bus capacity is {self.max_passengers} and it carries {len(self.passengers_on_board)} passengers")
        for passenger in self.passengers_on_board:
            print(passenger)

class Person:
    def __init__(self, name):
        self.name = name
        self.age = 0

bus_1 = Bus(3)
person_1 = Person("Kurt")
person_2 = Person("Mia")
person_3 = Person("Sophie")
person_4 = Person("David")

bus_1.passenger_waiting(person_1.name)
bus_1.add_passenger(person_1.name)
bus_1.passenger_waiting(person_2.name)
bus_1.add_passenger(person_2.name)
bus_1.passenger_waiting(person_3.name)
bus_1.add_passenger(person_3.name)
bus_1.passenger_waiting(person_4.name)
bus_1.add_passenger(person_4.name)
bus_1.show_details()

bus_1.remove_passenger()

bus_1.show_details()