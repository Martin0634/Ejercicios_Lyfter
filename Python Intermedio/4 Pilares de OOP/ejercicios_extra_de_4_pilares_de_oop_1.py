class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            print("Salary must be greater than zero.")
        else:
            self._salary = new_salary
    
    def promote(self, bonus):
        self.salary += float(self.salary) * (float(bonus) / 100)
        print(f"New salary is: {self.salary:.2f}")
        

def get_name():
    while True:
        try:
            user_input = input("Enter employee's name: ")
            if not user_input:
                raise ValueError("Name can't be blank.")
            elif len(user_input) < 3:
                raise ValueError("Name must be at least 3 characters long.")
            else:
                for i in user_input:
                    if i.isdigit():
                        raise ("Name can only have letters.")
                    else:
                        return user_input
        except ValueError as err:
            print(err)
            
def get_salary():
    while True:
        try:
            user_input = input("Enter employee's salary: $")
            if not user_input:
                raise ValueError("Salary can't be blank")
            elif not float(user_input):
                raise ValueError("Salary must be a valid number.")
            elif float(user_input) < 0:
                raise ValueError("Salary must be greater than zero.")
            elif '.' in user_input:
                if len(user_input.split('.')[1]) > 2:
                    raise ValueError("Salary can only have two decimals.")
            else:
                return float(user_input)
        except ValueError as err:
            print(err)

def get_new_salary():
    while True:
        try:
            user_input = input("Enter employee's salary: $")
            if not user_input:
                raise ValueError("Salary can't be blank")
            elif not float(user_input):
                raise ValueError("Salary must be a valid number.")
            elif '.' in user_input:
                if len(user_input.split('.')[1]) > 2:
                    raise ValueError("Salary can only have two decimals.")
            else:
                return float(user_input)
        except ValueError as err:
            print(err)

def create_employee():
    new_employee = Employee(
        name = get_name(),
        salary = get_salary()
    )
    print(f"Employee {new_employee.name} created.")
    print(f"{new_employee.name}'s salary is ${new_employee.salary:.2f}\n")
    return new_employee

def show_employee(employee):
    if not employee:
        print("Create employee first.")
    else:
        print (f"Employee's name is {employee.name} and employee's salary is: ${employee.salary:.2f}")

def modify_salary(employee):
    if not employee:
        print("Create employee first.")
    else:
        new_salary = get_new_salary()
        employee.salary = new_salary

def get_increment_rate(employee):
    if not employee:
        print("Create employee first.")
    else:
        while True:
            try:
                increment_rate = input("Enter increment %: ")
                if float(increment_rate) < 0:
                    raise ValueError("Increment % must be grater than zero.")
                else:
                    return increment_rate
            except ValueError as err:
                print(err)

def main_menu():
    employee = ''
    while True:
        print("----------DEMO-----------")
        print("------EMPLOYEE MENU------")
        print("1. Create employee")
        print("2. Modify salary")
        print("3. Promote  employee")
        print("4. Show  employee")
        print("E. Exit demo")
        user_input = input("\nChoose your option: ")
        
        if user_input == '1':
            employee = create_employee()
        
        elif user_input == '2':
            modify_salary(employee)
        
        elif user_input == '3':
            if not employee:
                print("Create employee first.")
            else:
                increment_rate = get_increment_rate(employee)
                employee.promote(increment_rate)
        
        elif user_input == '4':
            show_employee(employee)
        
        elif user_input == 'e' or user_input == 'E':
            print("Thanks for trying this demo.\nHave a nice day!")
            return False

        else:
            print("Invalid option. Try again.")

def main():
    main_menu()

if __name__ == '__main__':
    main()