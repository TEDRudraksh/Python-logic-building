# 8. Salary Tax Calculator
# Problem Statement

# Tax calculation differs by employee category.

# Create:

# abstract class TaxPayer

# Child:

# GovernmentEmployee
# PrivateEmployee
# Freelancer


from abc import ABC,abstractmethod
class TaxPayer(ABC):

    @abstractmethod
    def calc_tax(self):
        pass


class GovernmentEmployee(TaxPayer):

    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary


    def calc_tax(self):
        print("Tax - Government Employee")
        print(f"Name : {self.__name}")
        print(f"Salary : {self.__salary}")
        if self.__salary>=40000:
            print(f"Tax Amount : {self.__salary*0.02}")
        else:
            print("Not in Tax Slab")

class PrivateEmployee(TaxPayer):

    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary


    def calc_tax(self):
        print("Tax - Private Employee")
        print(f"Name : {self.__name}")
        print(f"Salary : {self.__salary}")
        if self.__salary>=40000:
            print(f"Tax Amount : {self.__salary*0.05}")
        else:
            print("Not in Tax Slab")


class Freelancer(TaxPayer):

    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary


    def calc_tax(self):
        print("Tax - Freelancer Employee")
        print(f"Name : {self.__name}")
        print(f"Salary : {self.__salary}")
        if self.__salary>=40000:
            print(f"Tax Amount : {self.__salary*0.08}")
        else:
            print("Not in Tax Slab")



print("1 for Government Employee")
print("2 for Private Employee")
print("3 for Freelancer\nEnter choice : ")
choice = int(input())
tax = None
if choice == 1:
    tax = GovernmentEmployee("Rudraksh",45000)
    
elif choice == 2:
    tax = PrivateEmployee()
    
elif choice == 3:
    tax = Freelancer()

tax.calc_tax()