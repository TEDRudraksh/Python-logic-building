# 9. Food Billing System
# Problem Statement

# Restaurants apply different GST percentages.

# Create:

# abstract class FoodItem

# Child:

# VegFood
# NonVegFood
# Beverage

# Rules:

# Veg → 5%
# NonVeg → 12%
# Beverage → 18%


from abc import ABC,abstractmethod
class FoodItem(ABC):

    @abstractmethod
    def gst_rate(self):
        pass


class VegFood(FoodItem):

    def __init__(self,name,price,quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__total = 0


    def bill(self):
        self.__total = self.__price*self.__quantity
        print(self.__total)


    def gst_rate(self):
        print(self.__total*0.05)

    def total_bill(self):
        self.bill()
        print(self.__total + self.__total*0.05)



class NonVegFood(FoodItem):

    def __init__(self,name,price,quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__total = 0


    def bill(self):
        self.__total = self.__price*self.__quantity
        print(self.__total)


    def gst_rate(self):
        print(self.__total*0.05)

    def total_bill(self):
        self.bill()
        print(self.__total + self.__total*0.12)


class Beverage(FoodItem):

    def __init__(self,name,price,quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__total = 0


    def bill(self):
        self.__total = self.__price*self.__quantity
        print(self.__total)


    def gst_rate(self):
        print(self.__total*0.05)

    def total_bill(self):
        self.bill()
        print(self.__total + self.__total*0.18)
    


print("1 for VegFood ")
print("2 for NonVegFood")
print("3 for Beverage \nEnter choice : ")
choice = int(input())
food = None
if choice == 1:
    food = VegFood("Noodles",120,2)
    
elif choice == 2:
    food = NonVegFood()
    
elif choice == 3:
    food= Beverage()

food.total_bill()