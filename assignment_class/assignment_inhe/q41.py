# 41. Cab Booking Application

# Features:

# User booking
# Driver assignment
# Fare calculation

# Use:

# inheritance
# abstraction
# polymorphism

from abc import ABC,abstractmethod

class RideBook(ABC):

    @abstractmethod
    def fare(self):
        pass

    @abstractmethod
    def driver(self):
        pass


class BikeRide(RideBook):

    def __init__(self,km):
        self.__km = km
        self.__rate = 10
    def fare(self):
        print("Your Bike Ride Fare")
        print(self.__km*self.__rate)

    def driver(self):
        print("Driver is Popatlal")


class CabRide(RideBook):

    def __init__(self,km):
        self.__km = km
        self.__rate = 15
    def fare(self):
        print("Your Cab Ride Fare")
        print(self.__km*self.__rate)

    def driver(self):
        print("Driver is Jethalal")


class AutoRide(RideBook):

    def __init__(self,km):
        self.__km = km
        self.__rate = 12
    def fare(self):
        print("Your Auto Ride Fare")
        print(self.__km*self.__rate)

    def driver(self):
        print("Driver is Sodhi")

print("1 for using Bike Ride")
print("2 for using Cab Ride")
print("3 for Auto Ride\nEnter choice : ")
choice = int(input())
f = None
if choice == 1:
    f = BikeRide(5)
    
elif choice == 2:
    f = CabRide(5)
    
elif choice == 3:
    f = AutoRide(5)

f.fare()