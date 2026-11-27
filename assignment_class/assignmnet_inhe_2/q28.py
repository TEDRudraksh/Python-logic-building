# 28. Transport Ticket Pricing
# Problem Statement

# Transport fares differ.

# Create:

# Bus
# Train
# Flight


from abc import ABC,abstractmethod

class Ride(ABC):

    @abstractmethod
    def fare(self):
        pass


class Bus(Ride):

    def __init__(self,km):
        self.__km = km
        self.__rate = 2
    def fare(self):
        print("Your Bus Ride Fare")
        print(self.__km*self.__rate)


class Train(Ride):

    def __init__(self,km):
        self.__km = km
        self.__rate = 0.50
    def fare(self):
        print("Your Train Ride Fare")
        print(self.__km*self.__rate)

class Flight(Ride):

    def __init__(self,km):
        self.__km = km
        self.__rate = 10
    def fare(self):
        print("Your Flight Ride Fare")
        print(self.__km*self.__rate)


print("1 for Bus Ride")
print("2 for Train Ride")
print("3 for Flight Ride\nEnter choice : ")
choice = int(input())
f = None
if choice == 1:
    f = Bus(5)
    
elif choice == 2:
    f = Train(5)
    
elif choice == 3:
    f = Flight(5)

f.fare()