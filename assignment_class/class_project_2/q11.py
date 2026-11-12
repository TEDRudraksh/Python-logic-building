# 11. E-Commerce Product System
# Problem

# Create product system for online store.

# Requirements

# Each product should have:

# product name
# price
# category
# Functionalities
# Apply GST using static method
# Apply category discount
# Display final price
# Concepts Practiced
# static methods
# calculations
# reusable logic


class Product:

    __category_set = {"clothing","dairy"}


    def __init__(self,name,category,price):
        self.__name = name
        self.__category = category
        self.__price = price
        self.__total = 0

    @staticmethod
    def gst(amount):
        return amount + (amount*0.10)

    def category(self):
        if self.__category in Product.__category_set:
            self.__price =  self.__price - (self.__price*.10)
            return self.__price

        else:
            self.__price = self.__price - (self.__price*.05)
            return self.__price


    def calculate(self):
        self.__price = self.category()
        print(self.__price)
        self.__total = Product.gst(self.__price)
        print(self.__total)
        

prod1 = Product("milk","dairy",100)
prod1.calculate()

