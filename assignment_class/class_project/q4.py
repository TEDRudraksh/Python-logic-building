# Car Info Manager
# Create a class Car with fields: brand, model, and year.
# Use setters to assign values. Create a method to print full car info.

class CarInfo:
    def __init__(self,brand=None,model=None,year=None):
        self.__brand = brand
        self.__model = model
        self.__year = year
 

    def set_details(self):
        brand = (input("brand name : "))
        self.__brand = brand

        model = (input("model no : "))
        self.__model = model

        year = int(input("year : "))
        self.__year = year
        
    def get_details(self):
        print("CAR INFO")
        print(f" brand : {self.__brand}")
        print(f" model : {self.__model}")
        print(f" year : {self.__year}")

car = CarInfo()
car.set_details()
car.get_details()