# 3. Electricity Bill Generator
# Problem Statement

# Electricity bills are calculated differently for:

# Residential users
# Commercial users
# Industrial users

# Create abstract class ElectricityBill.

# Rules
# Residential:
# Bill=Units×5

# Commercial:
# Bill=Units×8

# Industrial:
# Bill=Units×12

# Concepts
# Runtime polymorphism
# Real-world billing logic



from abc import ABC,abstractmethod

class ElectricityBill(ABC):

    @abstractmethod
    def bill(self):
        pass


class Residential(ElectricityBill):

    def __init__(self,units):
        self.__units = units
        self.__rate = 5

    def bill(self):
        print("Your Electricity Bill - Residential")
        print(self.__units*self.__rate)



class Commercial(ElectricityBill):

    def __init__(self,units):
        self.__units = units
        self.__rate = 8

    def bill(self):
        print("Your Electricity Bill - Commercial")
        print(self.__units*self.__rate)



class Industrial(ElectricityBill):

    def __init__(self,units):
        self.__units = units
        self.__rate = 12

    def bill(self):
        print("Your Electricity Bill - Industrial")
        print(self.__units*self.__rate)

print("1 for Residential Bill")
print("2 for Commercial Bill")
print("3 for Industrial Bill\nEnter choice : ")
choice = int(input())
f = None
if choice == 1:
    f = Residential(5)
    
elif choice == 2:
    f = Commercial(5)
    
elif choice == 3:
    f = Industrial(5)

f.bill()