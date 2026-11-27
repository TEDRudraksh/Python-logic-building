# 1. Employee Bonus Calculator
# Problem Statement

# A company gives bonuses differently based on employee type.

# Create:

# abstract class Employee
# child classes:
# Developer
# Manager
# Intern

# Rules:

# Developer → 20% bonus
# Manager → 35% bonus
# Intern → fixed ₹5000 bonus
# Requirements

# Methods:

# calculate_bonus()
# display_details()
# Concepts
# Abstract class
# Method overriding
# Business logic


from abc import ABC,abstractmethod
class Employee(ABC):

    @abstractmethod
    def calculate_bonus(self):
        pass

    @abstractmethod
    def display_details(self):
        pass



class Developer(Employee):

    def __init__(self,salary):
        self.__salary = salary
        self.__bonus =  0.20
    def calculate_bonus(self):
        print("Your Bonus")
        print(self.__salary*self.__bonus)
    def display_details(self):
        print(f"Salary : {self.__salary}")
        print(f"Bonus : {self.__salary*self.__bonus}")

class Manager(Employee):

    def __init__(self,salary):
        self.__salary = salary
        self.__bonus =  0.35
    def calculate_bonus(self):
        print("Your Bonus")
        print(self.__salary*self.__bonus)

    def display_details(self):
        print(f"Salary : {self.__salary}")
        print(f"Bonus : {self.__salary*self.__bonus}")


class Intern(Employee):

    def __init__(self,salary):
        self.__salary = salary
        self.__bonus =  5000
    def calculate_bonus(self):
        print("Your Bonus")
        print(self.__bonus)

    def display_details(self):
        print(f"Salary : {self.__salary}")
        print(f"Bonus : {self.__bonus}")



print("1 for Developer Bonus")
print("2 for Manager Bonus")
print("3 for Intern Bonus\nEnter choice : ")
choice = int(input())
f = None
if choice == 1:
    f = Developer(40000)
    
elif choice == 2:
    f = Manager(50000)
    
elif choice == 3:
    f = Intern(10000)

f.calculate_bonus()
f.display_details()