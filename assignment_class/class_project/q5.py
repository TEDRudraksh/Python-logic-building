# Product Inventory
# Create a class Product with fields: productId, name, quantity, price.
# Use setters to assign values. Add a method to calculate total value (quantity * price).


class ProductInventory:
    def __init__(self,productId=None, name=None, quantity=None, price=None):
        self.__productId = productId
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    def set_product_details(self):
        productId = int(input("Enter ProductId : "))
        self.__productId=  productId 

        name = (input("Enter Name : "))
        self.__name = name

        quantity = int(input("Enter Quantity : "))
        self.__quantity = quantity

        price = int(input("Enter Price : "))
        self.__price = price

    def total_value(self):
        total = self.__quantity*self.__price
        print(f" total {total}")

product = ProductInventory()
product.set_product_details()
product.total_value()