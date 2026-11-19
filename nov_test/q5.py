# Q5. OOP Programming Question: Product Management System
# Intermediate Level
#  10 Marks


# Problem Statement:

# Develop a Product Management System using Python OOP concepts.

# Create a class named Product with the following attributes:
# - product_id
# - product_name
# - category
# - price
# Requirements
# 1. Create a Product class with an appropriate constructor.
# 2. Create at least 5 product objects with different prices.
# 3. Store all product objects inside a list.
# 4. Implement a method display_product() to display product details.
# 5. Find and display the product having the second-highest price.
# 6. Display all products whose price is greater than ₹10,000.
# 7. Calculate and display the average price of all products.
# 8. Product must be unique on the basis of id


class Product:

    __product_lst = []
    

    def __init__(self,product_id,product_name,category,price):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__category = category
        self.__price = price
        if self.__product_id in Product.__product_lst:
            print("error")
        dic = {"id":self.__product_id,"prod_name":self.__product_name,"category":self.__category,"price":self.__price}
        Product.__product_lst.append(dic)


    @classmethod
    def add_prodcut_obj(cls,prod):
        cls.__product_lst.append(prod)


    def display_product(self):
        print("Product Deatils")
        print(f"Product_id : {self.__product_id}\nproduct_name : {self.__product_name}\ncategory : {self.__category}\nprice : {self.__price}")


    def second_high(self):
        print("Second Highest Product")
        high = float("-inf")
        low = float("-inf")
        for i in range(len(self.__product_lst)):
            if self.__product_lst[i]["price"]>high:
                high = self.__product_lst[i]["price"]
            elif self.__product_lst[i]["price"]<high and self.__product_lst[i]["price"]>low:
                low = high

        print(high)
        print(low)

    def price_10000(self):
        print("All Product greater than 10000")
        for i in range(len(self.__product_lst)):
            if self.__product_lst[i]["price"]>10000:
                print(self.__product_lst[i])



    def avg(self):
        total = 0
        print("Average Price of All products")
        for i in range(len(self.__product_lst)):
            if self.__product_lst[i]["price"]:
                total+=self.__product_lst[i]["price"]

        print(total/len(self.__product_lst))


p1 = Product("1122","laptop","elec",10000)
p2 = Product("1123","top","cloth",1000)
p3 = Product("1124","jeans","cloth",100)
p4 = Product("1125","car","auto",100000)
p5 = Product("1126","charger","elec",10)

p1.display_product()
p1.second_high()
p1.avg()
p1.price_10000()