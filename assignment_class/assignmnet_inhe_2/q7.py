
# 7. Cab Fare Calculator
# Problem Statement

# Cab fares differ based on ride type.

# Create:

# abstract class Ride

# Child:

# MiniRide
# SedanRide
# SUVRide

# Rules:

# Mini → ₹10/km
# Sedan → ₹15/km
# SUV → ₹20/km



from abc import ABC,abstractmethod

class Ride(ABC):

    @abstractmethod
    def fare(self):
        pass

class MiniRide(Ride):

    def __init__(self,km):
        self.__km = km
        self.__rate = 10

    def fare(self):
        print("Your Mini RideFare")
        print(self.__km*self.__rate)



class SedanRide(Ride):

    def __init__(self,km):
        self.__km = km
        self.__rate = 15

    def fare(self):
        print("Your Sedan Ride Fare")
        print(self.__km*self.__rate)



class SUVRide(Ride):

    def __init__(self,km):
        self.__km = km
        self.__rate = 20

    def fare(self):
        print("Your SUV Ride Fare")
        print(self.__km*self.__rate)


print("1 for Mini Ride")
print("2 for Sedan Ride")
print("3 for SUV Ride\nEnter choice : ")
choice = int(input())
f = None
if choice == 1:
    f = MiniRide(5)
    
elif choice == 2:
    f = SedanRide(5)
    
elif choice == 3:
    f = SUVRide(5)

f.fare()