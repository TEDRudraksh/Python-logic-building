# 21. Online Subscription Plans
# Problem Statement

# Streaming app has multiple subscription plans.

# Create:

# abstract class Subscription

# Child:

# BasicPlan
# StandardPlan
# PremiumPlan


# Each has different:

# price
# screen limits

from abc import ABC,abstractmethod
class Subcription(ABC):

    @abstractmethod
    def plan(self):
        pass

    @abstractmethod
    def subscribe(self):
        pass

subcibed = []

class BasicPlan(Subcription):

    def __init__(self,name):
        self.__name = name
        self.__price = 199
        self.__limit = 2
        self.__plan = "basic"

    def plan(self):
        print("Basic Plan")
        print(f"Price : {self.__price}")
        print(f"Screen Limit : {self.__limit}")

    @classmethod
    def subscribe(cls,obj):
        if obj in subcibed:
            print("Already Subcribed")

        else:
            subcibed.append(obj)
            print("Sub Success")

class StandardPlan(Subcription):

    def __init__(self,name):
        self.__name = name
        self.__price = 499
        self.__limit = 4
        self.__plan = "Standard"

    def plan(self):
        print("Standard Plan ")
        print(f"Price : {self.__price}")
        print(f"Screen Limit : {self.__limit}")

    @classmethod
    def subscribe(cls,obj):
        if obj in subcibed:
            print("Already Subcribed")

        else:
            subcibed.append(obj)
            print("Sub Success")

class PremiumPlan(Subcription):

    def __init__(self,name):
        self.__name = name
        self.__price = 799
        self.__limit = 6
        self.__plan = "Premium"

    def plan(self):
        print("Premium Plan")
        print(f"Price : {self.__price}")
        print(f"Screen Limit : {self.__limit}")

    @classmethod
    def subscribe(cls,obj):
        if obj in subcibed:
            print("Already Subcribed")

        else:
            subcibed.append(obj)
            print("Sub Success")


p = PremiumPlan("Rudra")
PremiumPlan.subscribe(p)
PremiumPlan.subscribe(p)