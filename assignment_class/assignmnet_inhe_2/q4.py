# 4. Vehicle Parking Fee System
# Problem Statement

# Parking fees vary by vehicle type.

# Create:
# abstract class Vehicle

# Child classes:
# Bike
# Car
# Bus

# Rules:

# Bike → ₹10/hour
# Car → ₹30/hour
# Bus → ₹50/hour


from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def fare(self):
        pass


class Bike(Vehicle):

    def __init__(self,hour):
        self.__hour = hour
        self.__rate = 10

    def fare(self):
        print("Your Parking fee - bike")
        print(self.__hour*self.__rate)



class Car(Vehicle):

    def __init__(self,hour):
        self.__hour = hour
        self.__rate = 30

    def fare(self):
        print("Your Parking fee - Car")
        print(self.__hour*self.__rate)



class Bus(Vehicle):

    def __init__(self,hour):
        self.__hour = hour
        self.__rate = 50

    def fare(self):
        print("Your Parking fee - Bus")
        print(self.__hour*self.__rate)

print("1 for Bike Parking fee")
print("2 for Car Parking fee")
print("3 for Bus Parking fee\nEnter choice : ")
choice = int(input())
f = None
if choice == 1:
    f = Bike(5)
    
elif choice == 2:
    f = Car(5)
    
elif choice == 3:
    f = Bus(5)

f.fare()