# 3. Online Shopping Cart
# Problem

# Create a shopping cart system.

# Requirements

# A cart should:
# store customer name
# maintain list of products
# maintain total bill
# Functionalities
# Add product
# Remove product
# Calculate final amount
# Apply discount using static method
# Track total carts created
# Concepts Practiced
# list inside object
# object interaction
# static method
# class variable


class ShoppingCart:

    __cart_no = 0

    def __init__(self,name="",total=0):
        self.__name = name
        self.__total = total
        self.__product = []
        ShoppingCart.__cart_no+=1

    @staticmethod
    def discount(bill):
        if bill>=2000:
            return bill - (bill*.10)
        else:
            return bill

    def add_product(self,product):
        self.__product.append(product)
        print("Product Added")

    def rm_product(self,product):
        for prod in self.__product:
            if prod["name"] == product:
                self.__product.remove(prod)

    def calculate(self):
        for prod in self.__product:
            if prod["price"]:
                self.__total+=prod["price"]

        self.__total = ShoppingCart.discount(self.__total)


    def display(self):
        print(f"Name : {self.__name}\nList of Product : {self.__product}\nBill : {self.__total}")

    @classmethod
    def cart_count(cls):
        print(f"Total cart : {cls.__cart_no}")


cart = ShoppingCart("Rudrksh",0)
# # cart.add_product({"product":"mic","price":5000})
# # cart.add_product({"product":"phone","price":500})
# # cart.add_product({"product":"laptop","price":1000})
# # cart.calculate()
# # cart.display()
# cart = ShoppingCart()
cart = ShoppingCart()

ShoppingCart.cart_count()