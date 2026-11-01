
# Mobile Phone Store
# Create a class Mobile with fields: brand, model, price.
# Use setters to set values. Create a method to check if phone is affordable (price < 20000).



class Mobile:
    def __init__(self,brand="",model="",price=0):
        self.__brand = brand
        self.__model = model
        self.__price = price
 

    def set_details(self):
        brand = (input("brand name : "))
        self.__brand = brand

        model = (input("model : "))
        self.__model = model

        price = int(input("price : "))
        self.__price = price
        
    def affordable(self):
        if self.__price<=20000:
            print("MOBILE IS AFFORDABLE")
            print(f" brand : {self.__brand}")
            print(f" model : {self.__model}")
            print(f" price : {self.__price}")
        else:
            print("MOBILE IS EXPENSIVE")
            print(f" brand : {self.__brand}")
            print(f" model : {self.__model}")
            print(f" price : {self.__price}")


Mob = Mobile()
Mob.set_details()
Mob.affordable()