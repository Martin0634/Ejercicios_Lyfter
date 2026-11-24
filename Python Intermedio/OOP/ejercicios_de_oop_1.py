import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return ((self.radius) * (self.radius) * (math.pi))

def main():
    circle_radius = float(input("Enter radius (inch): "))
    circle = Circle(circle_radius)
    print(f"The circle of radius {circle.radius} inch is {circle.get_area():.2f} inch^2")

if __name__ == '__main__':
    main()