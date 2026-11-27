# 11. Shape Drawing Application
# Problem Statement

# A drawing app supports multiple shapes.

# Create abstract class Shape.

# Child:

# Circle
# Rectangle
# Triangle

# Each implements:

# draw()
# area()


import turtle
from abc import ABC,abstractmethod
class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass
        
class Circle(Shape):

    def draw(self):
        pen = turtle.Turtle()
        screen = turtle.Screen()
        pen.circle(100)
        pen.speed(3)
        turtle.exitonclick()

    def area(self):
        radius = int(input("Enter Radius"))
        print(f"Area : {3.14*radius*radius}")

class Reactangle(Shape):

    def draw(self):
        pen = turtle.Turtle()
        screen = turtle.Screen()
        pen.speed(3)
        for i in range(2):
            pen.forward(200)
            pen.left(90)
            pen.forward(100)
            pen.left(90)

        turtle.exitonclick()

    def area(self):
        length = int(input("Enter length"))
        breadth = int(input("Enter Breadth"))
        print(f"Area : {length*breadth}")

    
class Triangle(Shape):

    def draw(self):
        pen = turtle.Turtle()
        screen = turtle.Screen()
        for _ in range(3):
            pen.forward(100) 
            pen.left(120)  
        turtle.exitonclick()

    def area(self):
        length = int(input("Enter length"))
        breadth = int(input("Enter Breadth"))
        print(f"Area : {0.5*length*breadth}")

print("1 for Draw Cicle")
print("2 for Draw Reactangle")
print("3 for Draw Triangle\nEnter choice : ")
choice = int(input())
draww = None
if choice == 1:
    draww = Circle()
    
elif choice == 2:
    draww = Reactangle()
    
elif choice == 3:
    draww = Triangle()

draww.draw()