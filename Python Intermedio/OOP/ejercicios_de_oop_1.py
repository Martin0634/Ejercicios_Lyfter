class Circle:
    def __init__(self):
        self.radius = 0
    
    def get_area(self):
        return ((self.radius) * (self.radius) * 3.14)

circle = Circle()
circle.radius = int(input("Enter radius (inch): "))
print(f"The circle of radius {circle.radius}inch is {circle.get_area()}inch^2")