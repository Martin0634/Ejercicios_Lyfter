import random

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers_on_board = []
    
    def add_passenger(self, person):
        if len(self.passengers_on_board) >= self.max_passengers:
            print(f"Full bus! No room for {person.name} in this bus!")
        else:
            self.passengers_on_board.append(person)
            print(f"{person.name} is in the bus.")
            
    def remove_passenger(self):
        if len(self.passengers_on_board) == 0:
            print("No passengers on board.")
        else:
            passenger = random.randint(0, (len(self.passengers_on_board)-1))
            print(f"{self.passengers_on_board[passenger].name} got off the bus.")
            self.passengers_on_board.pop(passenger)
        
    def show_details(self):
        print(f"Bus capacity is {self.max_passengers} and it carries {len(self.passengers_on_board)} passengers")
        for passenger in self.passengers_on_board:
            print(passenger.name)

class Person:
    def __init__(self, name):
        self.name = name
        self.age = 0
    
    def passenger_waiting(self):
        print(f"{self.name} is waiting at the bus stop.")
        print(f"{self.name} wants to get into the bus.")

def main():
    bus_1 = Bus(3)
    person_1 = Person("Kurt")
    person_2 = Person("Mia")
    person_3 = Person("Sophie")
    person_4 = Person("David")

    bus_1.remove_passenger()
    person_1.passenger_waiting()
    bus_1.add_passenger(person_1)
    person_2.passenger_waiting()
    bus_1.add_passenger(person_2)
    person_3.passenger_waiting()
    bus_1.add_passenger(person_3)
    person_4.passenger_waiting()
    bus_1.add_passenger(person_4)
    bus_1.show_details()

    bus_1.remove_passenger()
    bus_1.show_details()

if __name__ == '__main__':
    main()