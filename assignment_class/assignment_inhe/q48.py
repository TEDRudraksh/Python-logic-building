# 48. Inventory Management System

# Features:

# stock
# suppliers
# billing

stock = []
suppliers = []
billing = []

class Inventory:

    def add_stock(self,obj):
        stock.append(obj)
        print("Stock Added")

    def add_supplier(self,obj):
        suppliers.append(obj)
        print("suppliers Added")

    def add_bill(self,obj):
        billing.append(obj)
        print("billing Added")


    def display_stock(self):
        for i in stock:
            i.display_s()

    def display_supplier(self):
        for i in suppliers:
            i.display_supplier()

    def display_bill(self):
        for i in billing:
            i.display_bill()

class Stock:

    def __init__(self,prodname,quantity,price):
        self.__prodname = prodname
        self.__quantity = quantity
        self.__price = price


    def display_s(self):
        print("Stock quanntity")
        print(f"Prodname : {self.__prodname}")
        print(f"Quantity : {self.__quantity}")
        print(f"price : {self.__price}")


    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    
class Suppliers:

    def __init__(self,name):
        self.__name = name

    def display_supp(self):
        print("Supplier Details")
        print(f"Name : {self.__name}")


class Billing(Stock):

    def __init__(self, prodname, quantity, price):
        super().__init__(prodname, quantity, price)
        self.__bill = 0
        self.__quantity = quantity


    def cal_bill(self):
        print("Bill")
        self.__bill = self.get_price()*self.get_quantity()
        print(self.__bill)




inv = Inventory()


s1 = Stock("Laptop", 10, 50000)
s2 = Stock("Mouse", 20, 500)


inv.add_stock(s1)
inv.add_stock(s2)



sup1 = Suppliers("ABC Electronics")
sup2 = Suppliers("XYZ Traders")


inv.add_supplier(sup1)
inv.add_supplier(sup2)

b1 = Billing("Laptop", 2, 50000)
b2 = Billing("Mouse", 5, 500)


inv.add_bill(b1)
inv.add_bill(b2)

inv.display_stock()