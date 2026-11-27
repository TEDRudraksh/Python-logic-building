# 20. Ticket Booking System
# Problem Statement

# Ticket prices differ by seat category.

# Create:

# abstract class Ticket

# Child:

# SilverTicket
# GoldTicket
# PlatinumTicket

from abc import ABC,abstractmethod
class Ticket(ABC):

    @abstractmethod
    def pricing(self):
        pass

    @abstractmethod
    def book(self):
        pass


booked_ticket= []

class SilverTicket(Ticket):

    __seats = 100

    def __init__(self,name,quantity):
        self.__name = name
        self.__quantity = quantity
        self.__price = 1000
        self.__total = 0
        self.__type = "Silver"


    def book(self,obj):
        if self.__seats>=self.__quantity:
            self.__seats-=self.__quantity
            self.__total = self.__quantity*self.__price
            booked_ticket.append(obj)
            print("Ticket Book")
        else:
            print("Not enough Seats")

    def display(self):
        print(f"Name : {self.__name}")
        print(f"total : {self.__total}")
        print(f"Type : {self.__type}")

    def pricing(self):
        print("Pricing for Silver Ticket")
        print(self.__price)


class GoldTicket(Ticket):

    __seats = 100

    def __init__(self,name,quantity):
        self.__name = name
        self.__quantity = quantity
        self.__price = 3000
        self.__total = 0
        self.__type = "Gold"

    def book(self,obj):
        if self.__seats>=self.__quantity:
            self.__seats-=self.__quantity
            self.__total = self.__quantity*self.__price
            booked_ticket.append(obj)
            print("Ticket Book")
        else:
            print("Not enough Seats")

    def display(self):
        print(f"Name : {self.__name}")
        print(f"total : {self.__total}")
        print(f"Type : {self.__type}")

    def pricing(self):
        print("Pricing for Gold Ticket ")
        print(self.__price)


class PlatinumTicket(Ticket):

    __seats = 100

    def __init__(self,name,quantity):
        self.__name = name
        self.__quantity = quantity
        self.__price = 5000
        self.__total = 0
        self.__type = "Platinum"

    def book(self,obj):
        if self.__seats>=self.__quantity:
            self.__seats-=self.__quantity
            self.__total = self.__quantity*self.__price
            booked_ticket.append(obj)
            print("Ticket Book")
        else:
            print("Not enough Seats")

    def display(self):
        print(f"Name : {self.__name}")
        print(f"total : {self.__total}")
        print(f"Type : {self.__type}")

    def pricing(self):
        print("Pricing for Platinum Ticket ")
        print(self.__price)


p = PlatinumTicket("Rudra",10)
s = SilverTicket("RR",5)

p.book(p)
s.book(s)
