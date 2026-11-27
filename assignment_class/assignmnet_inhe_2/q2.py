# 2. Delivery Charge Calculator
# Problem Statement

# A delivery company calculates delivery charges differently.

# Create:

# abstract class Delivery

# Child classes:

# BikeDelivery
# TruckDelivery
# DroneDelivery

# Rules:

# Bike → ₹5/km
# Truck → ₹15/km
# Drone → ₹20/km
# Input Example

# Distance = 10 km

# Expected Output
# Bike Delivery Charge = 50
# Truck Delivery Charge = 150


from abc import ABC,abstractmethod

class Delivery(ABC):

    @abstractmethod
    def charge(self):
        pass

class BikeDelivery(Delivery):

    def __init__(self,km):
        self.__km = km
        self.__rate = 5

    def charge(self):
        print("Your Bike Delivery charge")
        print(self.__km*self.__rate)



class TruckDelivery(Delivery):

    def __init__(self,km):
        self.__km = km
        self.__rate = 15

    def charge(self):
        print("Your Truck Delivery charge")
        print(self.__km*self.__rate)


class DroneDelivery(Delivery):

    def __init__(self,km):
        self.__km = km
        self.__rate = 20

    def charge(self):
        print("Your Drone Delivery charge")
        print(self.__km*self.__rate)


print("1 for Bike Delivery")
print("2 for Truck Delivery")
print("3 for Drone Delivery\nEnter choice : ")
choice = int(input())
f = None
if choice == 1:
    f = BikeDelivery(5)
    
elif choice == 2:
    f = TruckDelivery(5)
    
elif choice == 3:
    f = DroneDelivery(5)

f.charge()