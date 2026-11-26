# 7. Shopping Cart System

# Base:

# Product

# Derived:

# Electronics
# Grocery
# Clothing

# Apply discounts.

from abc import ABC,abstractmethod
class Product(ABC):
    @abstractmethod
    def details(self):
        pass


class Electronics(Product):

    def __init__(self,price,name,quantity):
        self.__price = price
        self.__quantity = quantity
        self.__name = name
        self.__discount = 0
    def details(self):
        print(f"name : {self.__name}\nPrice : {self.__price}\nQuantity : {self.__quantity}")

    def discount(self):
        self.__discount = self.__price*.10
        print(f"Original : {self.__price}")
        print(f"discount : {self.__discount}")
        print(f"New : {self.__price - self.__discount}")
        print(f"total : {(self.__price - self.__discount)*self.__quantity}")

class Grocery(Product):

    def __init__(self,price,name,quantity):
        self.__price = price
        self.__quantity = quantity
        self.__name = name
        self.__discount = 0
    def details(self):
        print(f"name : {self.__name}\nPrice : {self.__price}\nQuantity : {self.__quantity}")

    def discount(self):
        self.__discount = self.__price*.15
        print(f"Original : {self.__price}")
        print(f"discount : {self.__discount}")
        print(f"New : {self.__price - self.__discount}")
        print(f"total : {(self.__price - self.__discount)*self.__quantity}")


class Clothing(Product):

    def __init__(self,price,name,quantity):
        self.__price = price
        self.__quantity = quantity
        self.__name = name
        self.__discount = 0
    def details(self):
        print(f"name : {self.__name}\nPrice : {self.__price}\nQuantity : {self.__quantity}")

    def discount(self):
        self.__discount = self.__price*.05
        print(f"Original : {self.__price}")
        print(f"discount : {self.__discount}")
        print(f"New : {self.__price - self.__discount}")
        print(f"total : {(self.__price - self.__discount)*self.__quantity}")


c = Clothing(1000,"T-shirt",5)
c.details()
c.discount()