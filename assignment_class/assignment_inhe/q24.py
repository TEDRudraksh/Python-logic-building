# 24. ATM System

# Abstract:

# ATM

# Derived:

# SBIATM
# HDFCATM

# Implement banking operations.

from abc import ABC,abstractmethod


class ATM(ABC):

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdrawal(self):
        pass



class SBIATM(ATM):

    __count = 0

    def __init__(self,pin,balance,bank,account):
        self.__pin = pin
        self.__balace = balance
        self.__bank = bank
        self.__account = account


    def get_balance(self):
        print(self.__balace)
        return self.__balace

    def deposit(self,amount):
        if amount>0 and amount<10000:
            self.__balace = self.__balace + amount
            print("Deposit Success")
        else:
            print("Invalid Amount")

    def withdrawal(self,amount):
        if SBIATM.__count<5:
            if amount>self.__balace:
                print("Insufficent Balance")

            else:
                self.__balace-=amount
                print("Withdrawal Success")
                SBIATM.__count+=1
        else:
            print("You Exced Monthly limit P/T charges : 25rupee")
            if amount>self.__balace:
                print("Insufficent Balance")

            else:
                self.__balace-=(amount+25)
                print("Withdrawal Success")
                SBIATM.__count+=1

class HDFCATM(ATM):

    __count = 0

    def __init__(self,pin,balance,bank,account):
        self.__pin = pin
        self.__balace = balance
        self.__bank = bank
        self.__account = account


    def get_balance(self):
        print(self.__balace)
        return self.__balace

    def deposit(self,amount):
        if amount>0 and amount<10000:
            self.__balace = self.__balace + amount
            print("Deposit Success")
        else:
            print("Invalid Amount")

    def withdrawal(self,amount):
        if HDFCATM.__count<7:
            if amount>self.__balace:
                print("Insufficent Balance")

            else:
                self.__balace-=amount
                print("Withdrawal Success")
                HDFCATM.__count+=1
        else:
            print("You Exced Monthly limit P/T charges : 25rupee")
            if amount>self.__balace:
                print("Insufficent Balance")

            else:
                self.__balace-=(amount+25)
                print("Withdrawal Success")
                HDFCATM.__count+=1

h = HDFCATM("1122",10000,"hdfc","3456")
h.get_balance()
h.withdrawal(1000)