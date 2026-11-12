# 14. Restaurant Billing System
# Problem

# Create restaurant order system.

# Requirements

# Each order:

# table number
# ordered items
# prices
# Functionalities
# Add items
# Remove items
# Calculate total bill
# Add service tax using static method

class Restaurant:
    def __init__(self,number):
        self.__number = number
        self.__orderItems = []
        self.__total = 0

    def add_items(self,name,price):
        # name = input("Enter Item Name")
        self.__name = name

        # price = int(input("Enter Item Price"))
        self.__price = price

        dic =  {"name":name,"price":price}
        self.__orderItems.append(dic)

    def rm_item(self):
        name = input("Enter item want to remove")
        for rm in self.__lst:
            if rm["name"] == name:
                self.__orderItems.remove(rm)
            else:
                print("Invalid Item")


    def calculate(self):
        ok = True
        for item in self.__orderItems:
            if item["price"]:
                self.__total+=item["price"]
                ok = False

        if ok:
            print("No item in Order")

    def display(self):
        print(self.__total)

item = Restaurant(10)
item.add_items("French",100)
item.add_items("FrenchFries",200)
item.calculate()
item.display()