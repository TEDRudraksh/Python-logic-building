# 50. Cryptocurrency Wallet System

# Features:

# wallet
# transactions
# deposits
# withdrawals

# Implement secure transaction architecture.


class Wallet:

    def __init__(self,name,balance):
        self.__name = name
        self.__balance = balance


    def funds(self):
        print(self.__balance)
        return self.__balance

    def add_funds(self,amount):
        self.__balance+=amount

    def remove_funds(self,amount):
        self.__balance-=amount

    def name(self):
        return self.__name


class Transactions:

    def __init__(self,sender,reciever,amount):
        self.__sender = sender
        self.__reciever = reciever
        self.__amount = amount


    def deposit(self,obj):
        if self.__amount>=1:
            obj.add_funds(self.__amount)
            print("Deposit Sucess")
        else:
            print("Error")


    def withdrawal(self,obj):
        if obj.funds()>self.__amount:
            obj.remove_funds(self.__amount)
            print("Withdrawal Sucess")
        else:
            print("ERROR 2")


w = Wallet("Rudra",10000)
w.funds()

t1 = Transactions("RR","Rudra",2000)
t2 = Transactions("tt","Rudra",1000)

t1.deposit(w)
t2.withdrawal(w)

w.funds()