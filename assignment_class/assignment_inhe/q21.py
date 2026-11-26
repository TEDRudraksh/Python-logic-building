# 21. Shape Area Calculator

# Abstract class Shape.

# Derived:

# Circle
# Rectangle
# Triangle

# Implement area calculation.

from abc import ABC,abstractmethod
class Shape(ABC):

    @abstractmethod
    def get_area(self):
        pass

        
class Circle(Shape):

    def get_area(self):
        print("Area of Circle")
        r = float(input("Enter Radius"))
        print("Result")
        print(3.14*r*r)


class Reactangle(Shape):

    def get_area(self):
        print("Area of Reactangle")
        l = float(input("Enter length"))
        w = float(input("Enter width"))
        print("Result")
        print(l*w)

class Triangle(Shape):

    def get_area(self):
        print("Area of Triangle")
        b = float(input("Enter base"))
        h = float(input("Enter higth"))
        print("Result")
        print(0.5*b*h)

print("1 for using Cicle")
print("2 for using Reactangle")
print("3 for using Triangle\nEnter choice : ")
choice = int(input())
area = None
if choice == 1:
    area = Circle()
    
elif choice == 2:
    area = Reactangle()
    
elif choice == 3:
    area= Triangle()

area.get_area()