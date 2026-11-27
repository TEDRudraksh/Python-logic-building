# 29. Insurance Premium Calculator
# Problem Statement

# Insurance premium varies.

# Create:

# HealthInsurance
# CarInsurance
# LifeInsurance

from abc import ABC,abstractmethod

class Insurance(ABC):

    @abstractmethod
    def preminum(self):
        pass



class HealthInsurance(Insurance):
    def __init__(self):
        self.__price = 1500
        self.__dieases = False

    def preminum(self):
        print("Preminum for Health Insurance")
        print(f"{self.__price}/Month")
        

class CarInsurance(Insurance):
    def __init__(self):
        self.__price = 1000
        self.__dieases = False

    def preminum(self):
        print("Preminum for CarInsurance ")
        print(f"{self.__price}/Month")


class LifeInsurance(Insurance):
    def __init__(self):
        self.__price = 400
        self.__dieases = False

    def preminum(self):
        print("Preminum for Life Insurance")
        print(f"{self.__price}/Month")
        

l = LifeInsurance()
l.preminum()