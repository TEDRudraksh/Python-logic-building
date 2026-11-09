# 16. Write a program to create a class called "Shape" with abstract methods for calculating area and perimeter, 
# and subclasses for "Rectangle", "Circle", and "Triangle".


import math

class Shape:

    def area(self, obj):
        if isinstance(obj, Rectangle):
            return obj.length * obj.breadth

        elif isinstance(obj, Circle):
            return math.pi * obj.radius ** 2

        elif isinstance(obj, Triangle):
            s = (obj.a + obj.b + obj.c) / 2
            return math.sqrt(s * (s-obj.a) * (s-obj.b) * (s-obj.c))

    def perimeter(self, obj):
        if isinstance(obj, Rectangle):
            return 2 * (obj.length + obj.breadth)

        elif isinstance(obj, Circle):
            return 2 * math.pi * obj.radius

        elif isinstance(obj, Triangle):
            return obj.a + obj.b + obj.c


class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth


class Circle:

    def __init__(self, radius):
        self.radius = radius


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c



s = Shape()
r = Rectangle(10, 5)
c = Circle(7)
t = Triangle(3, 4, 5)

print("Rectangle Area:", s.area(r))
print("Rectangle Perimeter:", s.perimeter(r))

print("Circle Area:", s.area(c))
print("Circle Perimeter:", s.perimeter(c))

print("Triangle Area:", s.area(t))
print("Triangle Perimeter:", s.perimeter(t))