from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def calculate_perimeter(self):
        return(self.radius*2*3.14)
    
    def calculate_area(self):
        return (3.14*self.radius*self.radius)

class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side
    
    def calculate_perimeter(self):
        return (4*self.side)
    
    def calculate_area(self):
        return (self.side * self.side)

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    
    def calculate_perimeter(self):
        return ((self.width*2)+(self.height*2))
    
    def calculate_area(self):
        return (self.width * self.height)

def get_user_data(data_type):
    while True:
        try:
            user_data = input(f"Enter {data_type} in inches: ").strip()
            for i in user_data:
                if i.isalpha():
                    raise ValueError("Measure can only contain numbers.")
            if not float(user_data):
                raise ValueError("Measure must be a valid number.")
            elif float(user_data) < 0:
                raise ValueError("Measure must be greater than zero.")
            elif '.' in user_data:
                if len(user_data.split('.')[1]) > 2:
                    raise ValueError("Measure can only have two decimals.")
                else:
                    return float(user_data)
            else:
                return float(user_data)
        except ValueError as err:
            print(err)

def circle():
    circle_radius = get_user_data('circle radius')
    new_circle = Circle(radius=circle_radius)
    print(f"\nThe perimeter of a circle with radius {circle_radius} inches is: {new_circle.calculate_perimeter():.2f} inches")
    print(f"And the area of a circle with radius {circle_radius} inches is: {new_circle.calculate_area():.2f} inches^2")
    input("Press 'ENTER' to continue")

def square():
    square_side = get_user_data('square side')
    new_square = Square(side=square_side)
    print(f"\nThe perimeter of a square with side {square_side} inches is: {new_square.calculate_perimeter():.2f} inches")
    print(f"The area of a square with side {square_side} inches is: {new_square.calculate_area():.2f} inches^2")
    input("Press 'ENTER' to continue")

def rectangle():
    rectangle_width = get_user_data('rectangle width')
    rectangle_height = get_user_data('rectangle height')
    new_rectangle = Rectangle(width=rectangle_width, height=rectangle_height)
    print(f"\nThe perimeter of a rectangle with width {rectangle_width} inches and height {rectangle_height} inches is: {new_rectangle.calculate_perimeter():.2f} inches.")
    print(f"The area of a rectangle with width {rectangle_width} inches and height {rectangle_height} inches is: {new_rectangle.calculate_area():.2f} inches^2")
    input("Press 'ENTER' to continue")

def main_menu():
    while True:
        print("-----------------------------")
        print("----------MAIN MENU----------")
        print("\n1. Circle")
        print("2. Square")
        print("3. Rectangle")
        print("E. Exit\n")
        user_option = input("Select your option: ")
        
        if user_option == '1':
            circle()
        
        elif user_option == '2':
            square()
        
        elif user_option == '3':
            rectangle()
        
        elif user_option == 'E' or user_option == 'e':
            print("Thank you for using MartinZeta systems.\nHave a nice day!")
            return False
        else:
            print("Invalid option. Try again.")

def main():
    main_menu()

if __name__ == '__main__':
    main()