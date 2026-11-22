import random

class Person:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class Role:
    def __init__(self, role, area):
        self.role = role
        self.area = area

class Employee(Person, Role):
    employees_registered = []
    
    def __init__(self, id, name, email, role, area):
        Person.__init__(self, id, name, email)
        Role.__init__(self, role, area)
        
    def add_employee (self):
        Employee.employees_registered.append(self)

class Rewards:
    def __init__(self, rewards_level, status):
        self.rewards_level = rewards_level
        self.status = status

class Customer(Person, Rewards):
    customers_registered = []
    
    def __init__(self, id, name, email, rewards_level, status):
        Person.__init__(self, id, name, email)
        Rewards.__init__(self, rewards_level, status)
    
    def add_customer (self):
            Customer.customers_registered.append(self)

def get_user_input(field):
    while True:
        try:
            user_input = input(f"Enter {field}: ").strip()
            for i in user_input:
                if i.isdigit():
                    raise ValueError(f"{field.capitalize()} can not contain numbers.")
            if len(user_input) < 3:
                raise ValueError(f"{field.capitalize()} must be at least 3 characters long.")
            elif len(user_input) > 30:
                raise ValueError(f"{field.capitalize()} can not contain more than 30 characters.")
            else:
                return user_input
        except ValueError as err:
            print(err)

def get_id(person_type):
    #id = 'E-' + str(random.randint(1000, 9999)) if person_type == 'Employee' else 'C-' + str(random.randint(1000, 9999))
    while True:
        if person_type == 'Employee':
            id = 'E-' + str(random.randint(1000,9999))
            if len(Employee.employees_registered) == 0:
                return id
            else:
                for employee in Employee.employees_registered:
                    for key, value in employee.__dict__.items():
                        if key == 'id':
                            if value != id:
                                return id
        if person_type == 'Customer':
            id = 'C-' + str(random.randint(1000,9999))
            if len(Customer.customers_registered) == 0:
                return id
            else:
                for customer in Customer.customers_registered:
                    for key, value in customer.__dict__.items():
                        if key == 'id':
                            if value != id:
                                return id

def register_person(person):
    id = get_id(person)
    name = get_user_input('full name')
    email = get_user_input('email')
    if person == 'Employee':
        role = get_user_input('role')
        area = get_user_input('area')
        new_employee = Employee(
            id = id,
            name = name,
            email = email,
            role = role,
            area = area,
        )
        new_employee.add_employee()
        
    if person == 'Customer':
        rewards_level = get_user_input('rewards level')
        rewards_status = get_user_input('rewards status')
        new_customer = Customer(
            id = id,
            name = name,
            email = email,
            rewards_level = rewards_level,
            status = rewards_status,
        )
        new_customer.add_customer()

def show_employees():
    if len(Employee.employees_registered) == 0:
        print("No employees registered.")
    else:
        for employee in Employee.employees_registered:
            for keys, values in employee.__dict__.items():
                print(f"{keys}: {values}")

def show_customers():
    if len(Customer.customers_registered) == 0:
        print("No customers registered.")
    else:
        for customer in Customer.customers_registered:
            for keys, values in customer.__dict__.items():
                print(f"{keys}: {values}")

def get_id_input():
    while True:
        try:
            id_input = input("Enter ID to delete (Ex. E-0000): ")
            if len(id_input) != 6:
                raise ValueError("ID must be a 6-digit combination. (Ex. E-0000)")
            for i in range(2,len(id_input)):
                if not id_input[i].isdigit():
                    raise ValueError("ID last four characters must be numbers")
            if id_input[0] != 'E' and id_input[0] != 'e' and id_input[0] != 'C' and id_input[0] != 'c':
                raise ValueError("ID must start with 'E' or 'C' (Ex. E-0000)")
            elif id_input[1] != '-':
                raise ValueError("ID muts have a letter and a hyphen (Ex. E-0000)")
            else:
                return id_input
        except ValueError as err:
            print(err)

def delete_with_id(id):
    if id[0] == 'E' or id[0] == 'e':
        employee_deleted = False
        for employee in range(len(Employee.employees_registered)):
            for key, value in Employee.employees_registered[employee].__dict__.items():
                if key == 'id':
                    if id.upper() == value.upper():
                        Employee.employees_registered.pop(employee)
                        employee_deleted = True
        if employee_deleted:
            print("Employee deleted.")
        else:
            print(f"ID: {id} not found.")
    
    if id[0] == 'C' or id[0] == 'c':
        customer_deleted = False
        for customer in range(len(Customer.customers_registered)):
            for key, value in Customer.customers_registered[customer].__dict__.items():
                if key == 'id':
                    if id.upper() == value.upper():
                        Customer.customers_registered.pop(customer)
                        customer_deleted = True
        if customer_deleted:
            print("Customer deleted.")
        else:
            print(f"ID: {id} not found.")

def main_menu():
    while True:
        print("---------------------------")
        print("------REGISTER PERSON------")
        print("1. Register Employee")
        print("2. Register Customer")
        print("3. Show Employees")
        print("4. Show Customers")
        print("5. Delete with ID")
        print("E. Exit")
        user_input = input("\nChoose your option: ")
        
        if user_input == '1':
            register_person('Employee')
        
        elif user_input == '2':
            register_person('Customer')
        
        elif user_input == '3':
            show_employees()
            
        elif user_input == '4':
            show_customers()
        
        elif user_input == '5':
            delete_with_id(get_id_input())
        
        elif user_input == 'E' or user_input == 'e':
            print("\nThanks for using MartinZeta Systems.\nHave a nice day!")
            return False
        
        else:
            print("Invalid option. Try again.")

def main():
    main_menu()

if __name__ == '__main__':
    main()