
# Bank Account
# Create a class BankAccount with fields: accountNumber, holderName, balance.
# Use setters to assign values. Add a method to display balance.


class BankAccount:
    def __init__(self,accountNumber=None,holderName=None,balance=None):
        self.__accountNumber = accountNumber
        self.__holderName = holderName
        self.__balance = balance
 

    def set_details(self):
        accountNumber = int(input("enter account no : "))
        self.__accountNumber = accountNumber

        holderName = (input("enter your name : "))
        self.__holderName = holderName

        balance = int(input("enter your balance: "))
        self.__balance = balance
        
    def get_balance(self):
        print(f" balance : {self.__balance}")

bank = BankAccount()
bank.set_details()
bank.get_balance()