# 19. Courier Service Pricing
# Problem Statement

# Pricing depends on package type.

# Create:

# abstract class Courier

# Child:

# NormalCourier
# ExpressCourier
# SameDayCourier



from abc import ABC,abstractmethod

class Courier(ABC):

    @abstractmethod
    def pricing(self):
        pass

class NormalCourier(Courier):

    def __init__(self,km):
        self.__km = km
        self.__rate = 5

    def pricing(self):
        print("Your Normal Courier pricing")
        print(self.__km*self.__rate)



class ExpressCourier(Courier):

    def __init__(self,km):
        self.__km = km
        self.__rate = 10

    def pricing(self):
        print("Your Express Courier pricing")
        print(self.__km*self.__rate)



class SameDayCourier(Courier):

    def __init__(self,km):
        self.__km = km
        self.__rate = 20

    def pricing(self):
        print("Your Same Day Courier pricing")
        print(self.__km*self.__rate)



print("1 for Normal Courier")
print("2 for Express Courier")
print("3 for Same Day Courier\nEnter choice : ")
choice = int(input())
f = None
if choice == 1:
    f = NormalCourier(5)
    
elif choice == 2:
    f = ExpressCourier(5)
    
elif choice == 3:
    f = SameDayCourier(5)

f.pricing()