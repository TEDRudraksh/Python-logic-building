# 2. Bank Account Simulation
# Problem

# Design a banking system using OOP.

# Requirements

# Each account should contain:

# account number
# holder name
# balance
# Functionalities
# Deposit money
# Withdraw money
# Prevent withdrawal if balance insufficient
# Display account summary
# Maintain bank-wide interest rate as class variable
# Add static method to validate minimum balance rule
# Concepts Practiced
# object state management
# static methods
# class variables
# validations



class Account:

    __icici = 6
    __sbi = 5
    __cbi = 2

    def __init__(self,account_number,holder_name,balance):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    @staticmethod
    def balance_check(balance):
        if balance<=2000:
            return print("Minimum balace is not maintain")
        else:
            return print("Mininum Balance is Maintaned")

    def deposit(self,amount):
        self.__balance+=amount
        print("Amount Added")

    def withdrawal(self,amount):
        if self.__balance<amount:
            return print("Insuffiecnt Balance")
        self.__balance-=amount
        print("Withdrawal Success")

    def get_balance(self):
        return self.__balance

    def display(self):
        print(f"Name : {self.__holder_name}\nAccountNo : {self.__account_number}\nBalance : {self.__balance}")


acc = Account(1122,"rud",4500)
Account.balance_check(acc.get_balance())
acc.deposit(2000)
acc.withdrawal(1000)
acc.display()