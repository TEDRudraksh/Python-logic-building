# 18. Vehicle Insurance System
# Vehicle
# InsuredVehicle
# Car

# Calculate insurance amount.


class Vehicle:
    def __init__(self,tire,type_):
        self.__tire = tire
        self.__type = type_

    def get_type(self):
        return self.__type

    def get_tire(self):
        return self.__tire

class InsuredVehicle(Vehicle):
    def __init__(self, tire, type_,status):
        super().__init__(tire, type_)
        self.__status = status

    def rate(self):
        if self.get_type().lower() == "car":
            return 0.10
        elif self.get_type().lower() == "bike":
            return 0.05
        else:
            print("Not in list")
            return 0
    def get_status(self):
        return self.__status
    

class Car(InsuredVehicle):
    def __init__(self, tire, type_, status,carvalue):
        super().__init__(tire, type_, status)
        self.__carvalue = carvalue
    
    def amount(self):
        if self.get_status():
            print(f"Car Price : {self.__carvalue}")
            print("Insure Amount")
            print(f"{self.__carvalue*InsuredVehicle.rate(self)}")

        else:
            print("Your Vehicle is not insured ")

c = Car("4","Car",True,300000)
c.amount()