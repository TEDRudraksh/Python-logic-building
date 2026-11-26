# 10. Movie Ticket Booking

# Parent:

# Ticket

# Derived:

# GoldTicket
# PlatinumTicket
# VIPTicket

# Apply pricing logic.

from abc import ABC,abstractmethod

class Ticket(ABC):
    @abstractmethod
    def price(self):
        pass


class GoldTicket(Ticket):

    def __init__(self):
        self.__price = 1000

    def price(self):
        print("Base Ticket Price : 1000")
        self.__price = self.__price + self.__price*.10
        print("Golden Ticket Perks : Access for Food ")
        print(self.__price)


class PlatinumTicket(Ticket):

    def __init__(self):
        self.__price = 1000

    def price(self):
        print("Base Ticket Price : 1000")
        self.__price = self.__price + self.__price*.15
        print("Platinum Ticket Perks : Access for Food,1st Row Access,Goodies")
        print(self.__price)


class VIPTicket(Ticket):

    def __init__(self):
        self.__price = 1000

    def price(self):
        print("Base Ticket Price : 1000")
        self.__price = self.__price + self.__price*.20
        print("VIP Ticket Perks : Access for Food, fan box Access,Goodies,Players Signature,")
        print(self.__price)


v = VIPTicket()
v.price()