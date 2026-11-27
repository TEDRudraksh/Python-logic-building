# 26. Water Bill Calculator
# Problem Statement

# Water charges vary by usage type.

# Create:

# Residential
# Commercial
# Agricultural


from abc import ABC,abstractmethod

class WaterBill(ABC):

    @abstractmethod
    def bill(self):
        pass


class Residential(WaterBill):

    def __init__(self,units):
        self.__units = units
        self.__rate = 5

    def bill(self):
        print("Your WaterBill - Residential")
        print(self.__units*self.__rate)



class Commercial(WaterBill):

    def __init__(self,units):
        self.__units = units
        self.__rate = 8

    def bill(self):
        print("Your WaterBill - Commercial")
        print(self.__units*self.__rate)



class Industrial(WaterBill):

    def __init__(self,units):
        self.__units = units
        self.__rate = 12

    def bill(self):
        print("Your WaterBill  - Industrial")
        print(self.__units*self.__rate)

print("1 for Water Bill Residential ")
print("2 for Water Bill Commercial ")
print("3 for Water Bill Industrial\nEnter choice : ")
choice = int(input())
f = None
if choice == 1:
    f = Residential(5)
    
elif choice == 2:
    f = Commercial(5)
    
elif choice == 3:
    f = Industrial(5)

f.bill()