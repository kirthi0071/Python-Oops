class Shape():
    def area (self):
        print(" area not defined")


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        print(f"Area of rectangle: {self.width * self.length}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        print(f"Area of circle: {3.14 * self.radius ** 2}")

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print(f"Area of triangle: {0.5 * self.base * self.height}")

shapes =[Rectangle(5, 10), Circle(7), Triangle(6, 8)]

for shape in shapes:
    shape.area()
    
