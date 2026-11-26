
# 8. Online Food Delivery

# Parent:

# FoodItem

# Derived:

# Pizza
# Burger
# Sandwich

# Calculate total bill.


from abc import ABC,abstractmethod
class FoodItem(ABC):
    @abstractmethod
    def details(self):
        pass


class Pizza(FoodItem):

    def __init__(self,price,quantity):
        self.__price = price
        self.__quantity = quantity
        self.__total = 0
        self.__discount = 0
    def details(self):
        print(f"Price : {self.__price}\nQuantity : {self.__quantity}")

    def bill(self):
        self.__discount = self.__price*.10
        print(f"Original : {self.__price}")
        print(f"discount : {self.__discount}")
        print(f"New : {self.__price - self.__discount}")
        self.__total = (self.__price - self.__discount)*self.__quantity
        print(f"total : {self.__total}")


class Burger(FoodItem):

    def __init__(self,price,quantity):
        self.__price = price
        self.__quantity = quantity
        self.__total = 0
        self.__discount = 0
    def details(self):
        print(f"Price : {self.__price}\nQuantity : {self.__quantity}")

    def bill(self):
        self.__discount = self.__price*.10
        print(f"Original : {self.__price}")
        print(f"discount : {self.__discount}")
        print(f"New : {self.__price - self.__discount}")
        self.__total = (self.__price - self.__discount)*self.__quantity
        print(f"total : {self.__total}")


class Sandwich(FoodItem):

    def __init__(self,price,quantity):
        self.__price = price
        self.__quantity = quantity
        self.__total = 0
        self.__discount = 0
    def details(self):
        print(f"Price : {self.__price}\nQuantity : {self.__quantity}")

    def bill(self):
        self.__discount = self.__price*.10
        print(f"Original : {self.__price}")
        print(f"discount : {self.__discount}")
        print(f"New : {self.__price - self.__discount}")
        self.__total = (self.__price - self.__discount)*self.__quantity
        print(f"total : {self.__total}")


s =Sandwich(100,5)
s.details()
s.bill()