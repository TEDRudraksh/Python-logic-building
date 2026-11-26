# 27. Transport Fare System

# Abstract:

# Transport

# Derived:

# Train
# Flight
# Bus

# Implement ticket pricing.




from abc import ABC,abstractmethod

class Transport(ABC):

    @abstractmethod
    def ticket(self):
        pass


class Train(Transport):

    def __init__(self,km):
        self.__km = km
        self.__rate = 0.50
    def ticket(self):
        print("Your Train ticket pricing")
        print(self.__km*self.__rate)


class Flight(Transport):

    def __init__(self,km):
        self.__km = km
        self.__rate = 10
    def ticket(self):
        print("Your flight ticket pricing")
        print(self.__km*self.__rate)

class Bus(Transport):

    def __init__(self,km):
        self.__km = km
        self.__rate = 1
    def ticket(self):
        print("Your bus ticket pricing")
        print(self.__km*self.__rate)


print("1 for Train ")
print("2 for Flight")
print("3 for Bus\nEnter choice : ")
choice = int(input())
f = None
if choice == 1:
    f = Train(500)
    
elif choice == 2:
    f = Flight(500)
    
elif choice == 3:
    f = Bus(500)

f.ticket()