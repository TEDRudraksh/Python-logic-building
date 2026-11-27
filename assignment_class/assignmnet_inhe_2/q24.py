# 24. Ride Sharing App Surge Pricing
# Problem Statement

# Surge pricing differs.

# Create:

# abstract class RidePricing

# Child:

# NormalTime
# PeakTime
# RainTime


from abc import ABC,abstractmethod

class RidePricing(ABC):

    @abstractmethod
    def surge(self):
        pass

class NormalTime(RidePricing):

    def __init__(self):
        self.__rate = 5

    def surge(self):
        print("Your surge charge")
        print(f"{self.__rate}/km")



class PeakTime(RidePricing):

    def __init__(self):
        self.__rate = 8

    def surge(self):
        print("Your surge charge")
        print(f"{self.__rate}/km")



class RainTime(RidePricing):

    def __init__(self):
        self.__rate = 10

    def surge(self):
        print("Your surge charge")
        print(f"{self.__rate}/km")


r = RainTime()
r.surge()