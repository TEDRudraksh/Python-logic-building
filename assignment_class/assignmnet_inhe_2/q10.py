# 10. Loan Interest Calculator
# Problem Statement

# Banks offer different interest rates.

# Create:

# abstract class Loan

# Child:

# HomeLoan
# CarLoan
# EducationLoan

# Formula
# Interest=
# 100
# P×R×T
from abc import ABC,abstractmethod
class Loan(ABC):

    @abstractmethod
    def calc_Loan(self):
        pass


class HomeLoan(Loan):

    def __init__(self,name,principle,time):
        self.__name = name
        self.__principle = principle
        self.__time = time


    def calc_Loan(self):
        print("Your Home Loan Amount")
        print(f"base : {self.__principle}")
        print(f"Interset Amount : {(self.__principle*self.__time*(8/100))}")


class CarLoan(Loan):

    def __init__(self,name,principle,time):
        self.__name = name
        self.__principle = principle
        self.__time = time


    def calc_Loan(self):
        print("Your Car Loan Amount")
        print(f"base : {self.__principle}")
        print(f"Interset Amount : {(self.__principle*self.__time*(5/100))}")


class EducationLoan(Loan):

    def __init__(self,name,principle,time):
        self.__name = name
        self.__principle = principle
        self.__time = time


    def calc_Loan(self):
        print("Your Education Loan Amount")
        print(f"base : {self.__principle}")
        print(f"Interset Amount : {(self.__principle*self.__time*(3/100))}")


print("1 for Home Loan ")
print("2 for CarLoan")
print("3 for Education Loan\nEnter choice : ")
choice = int(input())
loan = None
if choice == 1:
    loan = HomeLoan()
    
elif choice == 2:
    loan = CarLoan()
    
elif choice == 3:
    loan= EducationLoan()

loan.calc_Loan()