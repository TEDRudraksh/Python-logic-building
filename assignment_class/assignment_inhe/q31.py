# 31. Drawable Interface

# Interface:

# draw()

# Implement:

# Circle
# Rectangle
# Line


import turtle
from abc import ABC,abstractmethod
class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass

        
class Circle(Shape):

    def draw(self):

        pen = turtle.Turtle()
        screen = turtle.Screen()
        pen.circle(100)
        pen.speed(3)
        turtle.exitonclick()


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

    
class Line(Shape):

    def draw(self):
        pen = turtle.Turtle()
        screen = turtle.Screen()
        pen.speed(3)
        pen.forward(100)
        turtle.exitonclick()

print("1 for Draw Cicle")
print("2 for Draw Reactangle")
print("3 for Draw Libe\nEnter choice : ")
choice = int(input())
draww = None
if choice == 1:
    draww = Circle()
    
elif choice == 2:
    draww = Reactangle()
    
elif choice == 3:
    draww= Line()

draww.draw()