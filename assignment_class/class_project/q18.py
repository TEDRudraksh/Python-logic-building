# 8. Write a  program to create class called "TrafficLight" with attributes for color and duration, and methods
#  to change the color and check for red or green.


class TrafficLight:
    def __init__(self,color="",duration=0):
        self.__color = color
        self.__duration = duration

    def change_color(self):
        newcolor = input("Enter New Color")
        self.__color = newcolor.lower()

        duration = int(input("Enter Duration"))
        self.__duration = duration

    def isRed(self):
        if self.__color == "red":
            print("Color is Red")

    def isGreen(self):
        if self.__color == "green":
            print("Color is Green")


traffic = TrafficLight()
traffic.change_color()
traffic.isGreen()
traffic.isRed()
    