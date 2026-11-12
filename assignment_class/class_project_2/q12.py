# 12. Car Rental System
# Problem

# Create a car rental platform.

# Requirements

# Each car:

# car number
# model
# rental price per day
# availability
# Functionalities
# Rent car
# Return car
# Calculate rent amount
# Prevent renting unavailable cars

class Car:

    def __init__(self,carNo,model,price,date):
        self.__carNo = carNo
        self.__model = model
        self.__price = price
        self.__total = 0
        self.__status = False
        self.__date = date



    def rent_car(self):
        if self.__status == False:
            print("Car Rented")
            self.__total = self.calculate()
            self.__status = True
        else:
            print("No Car for Rent")

    def return_car(self):
        if self.__status == True:
            print("Car Returned")
            self.__status = False
        else:
            print("No Car for Return")


    def calculate(self):
        self.__total = self.__price*self.__date
        print(self.__total)


rent = Car("Mazda100","XC100",200,10)
rent.return_car()
rent.rent_car()
rent.return_car()
rent.calculate()

