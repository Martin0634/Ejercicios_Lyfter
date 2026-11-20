class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        return (self.width * self.height)
    
    def get_perimeter(self):
        return ((self.width * 2)+(self.height * 2))

def validate_input():
    flag = True
    while flag:
        try:
            user_input = float(input("Enter (inch): "))
            if user_input <= 0:
                raise ValueError("Must be greater than zero")
            else:
                flag = False
                return user_input
        except ValueError as err:
            print(err)

def get_user_inputs():
    print("Enter rectangle's width and height: \n")
    return Rectangle(validate_input(), validate_input())
    
def main():
    rectangle_1 = get_user_inputs()
    print(f"Rectangles area is: {rectangle_1.get_area():.2f} inch^2")
    print(f"Rectangles perimeter is: {rectangle_1.get_perimeter():.2f} inch")

if __name__ == '__main__':
    main()