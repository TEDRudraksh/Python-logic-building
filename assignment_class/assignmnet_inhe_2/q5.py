# 5. Online Shopping Discount System
# Problem Statement

# Different customer types receive different discounts.

# Create:

# abstract class Customer

# Child:

# RegularCustomer
# PremiumCustomer
# VIPCustomer

# Rules:

# Regular → 5%
# Premium → 10%
# VIP → 20%




from abc import ABC,abstractmethod

class Customer(ABC):

    @abstractmethod
    def discount(self):
        pass

class Regular(Customer):

    def __init__(self,bill):
        self.__bill = bill
        self.__discount = 0.05

    def discount(self):
        print(f"Your Discount for bill : {self.__bill}")
        print(self.__bill*self.__discount)



class Premium(Customer):

    def __init__(self,bill):
        self.__bill = bill
        self.__discount = 0.10

    def discount(self):
        print(f"Your Discount for bill : {self.__bill}")
        print(self.__bill*self.__discount)


class VIP(Customer):

    def __init__(self,bill):
        self.__bill = bill
        self.__discount = 0.20

    def discount(self):
        print(f"Your Discount for bill : {self.__bill}")
        print(self.__bill*self.__discount)

print("1 for Regular Customer")
print("2 for Premium Customer")
print("3 for VIP Customer\nEnter choice : ")
choice = int(input())
f = None
if choice == 1:
    f = Regular(500)
    
elif choice == 2:
    f = Premium(500)
    
elif choice == 3:
    f = VIP(500)

f.discount()