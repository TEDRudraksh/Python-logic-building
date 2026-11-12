# 8. Inventory Management System
# Problem

# Create product inventory software.

# Requirements

# Each product should contain:

# product id
# product name
# quantity
# price
# Functionalities
# Add stock
# Reduce stock after purchase
# Prevent negative stock
# Calculate inventory value
# Concepts Practiced
# arithmetic inside classes
# validations
# inventory logic



class ProductInventory:
    def __init__(self,productId=0, name="", quantity=0, price=0):
        self.__productId = productId
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    def set_product_details(self,productId,name,quantity,price):
        # productId = int(input("Enter ProductId : "))
        self.__productId=  productId 

        # name = (input("Enter Name : "))
        self.__name = name

        # quantity = int(input("Enter Quantity : "))
        self.__quantity = quantity

        # price = int(input("Enter Price : "))
        self.__price = price
    def add_stock(self,no):
        self.__quantity+=no
        print("Stock added")


    def purchase(self,no):
        if self.__quantity>no:
            self.__quantity-=no
            print('Purchase Success')
        else:
            return print('Exceed Stock ')

    def total_value(self):
        total = self.__quantity*self.__price
        print(f" total inventory value {total}")

    def display(self):
        print(self.__name)
        print(self.__productId)
        print(self.__quantity)
        print(self.__price)        


product = ProductInventory()
product.set_product_details(1122,"rud",10,500)
product.display()
product.purchase(5)
product.display()
product.total_value()