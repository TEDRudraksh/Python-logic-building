# 13. Write a program to create a class called "Inventory" with a collection of products and methods
#  to add and remove products, and to check for low inventory.

class Inventory:
    def __init__(self,product=[]):
        self.__product = product


    def add_prod(self):
        name =input("Enter Product Name : ")
        quanitty = int(input("Enter Quantity : "))
        price = int(input("Enter Price : "))

        dic = {"name" : name, "quantity" : quanitty, "price" : price }
        self.__product.append(dic)

    def rm_prod(self):
        name =input("Enter Product Name to Remove: ")
        for rm in self.__product:
            if rm["name"] == name:
                self.__product.remove(rm)
            else:
                print("Does not Exist")


    def low_inventory(self):
        for low in self.__product:
            if low["quantity"]<=10:
                print(f"this products have low quantity  : {low}") 
            else:
                print(f"Products does not have low quantity : {low} ")

check = Inventory()
check.add_prod()
check.add_prod()
check.rm_prod()
check.low_inventory()
