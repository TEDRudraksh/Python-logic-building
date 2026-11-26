# 5. Banking System

# Parent:

# BankAccount

# Child:

# SavingsAccount
# CurrentAccount

# Implement withdrawal rules.

from abc import ABC,abstractmethod
class BankAccount(ABC):

    @abstractmethod
    def accountdetail(self):
        pass



class SavingAccount(BankAccount):

    def __init__(self,name,age,accountno):
        self.__name = name
        self.__age = age
        self.__accountno = accountno
        self.__balance = 0
        
    def accountdetail(self):
        print(f"name : {self.__name}\nAge : {self.__age}\nAccountno : {self.__accountno}")

    def balance(self):
        print(self.__balance)

    def deposit(self,amount):
        if amount>=1:
            self.__balance+= amount
            print("Deposit Sucess")
        else:
            print("Not valid")

    def withdrawal(self,amount):
        if amount>self.__balance:
            print("Not Enough Balance")
        else:
            self.__balance-=amount
            print("Withdrawal Success")



class CurrentAccount(BankAccount):

    def __init__(self,name,age,accountno):
        super.__init__(name,age,accountno)
        
    def accountdetail(self):
        print(f"name : {self.__name}\nAge : {self.__age}\nAccountno : {self.__accountno}")

    def balance(self):
        print(self.__balance)

    def deposit(self,amount):
        if amount>=1:
            self.__balance+= amount
            print("Deposit Sucess")
        else:
            print("Not valid")

    def withdrawal(self,amount):
        if amount>self.__balance:
            print("Not Enough Balance")
        else:
            self.__balance-=amount
            print("Withdrawal Success")


s = SavingAccount("R",10,1122)
s.balance()
s.accountdetail()
s.deposit(3000)
s.withdrawal(1000)
s.balance()