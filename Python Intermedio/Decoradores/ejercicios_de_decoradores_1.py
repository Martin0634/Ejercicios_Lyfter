class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def print_data(func):
            def wrapper(*args):
                print("This is the info:")
                func(*args)
                print("Thank you for interacting.")
            return wrapper
    
    @print_data
    def show_details(self):
        print(f"Width: {self.width} inches")
        print(f"Height: {self.height} inches")


def main():
    rectangle = Rectangle(6,7)
    rectangle.show_details()

if __name__ == '__main__':
    main()