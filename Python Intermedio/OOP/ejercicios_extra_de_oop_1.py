class Rectangle:
    def __init__(self):
        self.width = self.validate_input('width')
        self.height = self.validate_input('height')
    
    def get_area(self):
        return (self.width * self.height)
    
    def get_perimeter(self):
        return ((self.width * 2)+(self.height * 2))
    
    def validate_input(self, data):
        while True:
            try:
                user_input = float(input(f"Enter rectangle's {data} (inch): "))
                if user_input <= 0:
                    raise ValueError("Must be greater than zero")
                else:
                    return user_input
            except ValueError as err:
                print(err)
    
    def show_details(self):
        print(f"Rectangles area is: {self.get_area():.2f} inch^2")
        print(f"Rectangles perimeter is: {self.get_perimeter():.2f} inch")
    
def main():
    rectangle_1 = Rectangle()
    rectangle_1.show_details()

if __name__ == '__main__':
    main()