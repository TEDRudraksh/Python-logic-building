# 18. Write a program to create a class called "Restaurant" with attributes for menu items, prices, and ratings,
#  and methods to add and remove items, and to calculate average rating.

class Restaurant:
    def __init__(self):
        self.__lst = []
        self.__avg = 0

    def add_items(self):
        name = input("Enter Item Name")
        self.__name = name

        price = int(input("Enter Item Price"))
        self.__price = price

        rating = int(input("Enter Item Rating"))
        self.__rating = rating

        dic =  {"name":name,"price":price,"rating":rating}
        self.__lst.append(dic)

    def rm_item(self):
        name = input("Enter item want to remove")
        for rm in self.__lst:
            if rm["name"] == name:
                self.__lst.remove(rm)
            else:
                print("Invalid Item")


    def calculate(self):
        print("Avg Rating")
        for item in self.__lst:
            if item["rating"]:
                self.__avg += item["rating"]

        self.__avg=(self.__avg)/len(self.__lst)
        print(f"Avg : {self.__avg}")

item = Restaurant()
item.add_items()
item.add_items()
item.add_items()
item.calculate()