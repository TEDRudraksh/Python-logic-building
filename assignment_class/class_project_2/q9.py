# 9. ATM Machine Simulation
# Problem

# Design ATM software.

# Requirements

# Each account should have:

# account number
# PIN
# balance
# Functionalities
# Login verification
# Withdraw
# Deposit
# Change PIN
# Mini statement
# Additional Challenge

# Lock account after 3 wrong PIN attempts.

# Concepts Practiced
# encapsulation mindset
# validations
# object state



class BankAccount:
    def __init__(self,accountNumber="",pin="",balance=0):
        self.__accountNumber = accountNumber
        self.__pin = pin
        self.__balance = balance
        self.__login = False
 

    def set_details(self):
        accountNumber = int(input("enter account no : "))
        self.__accountNumber = accountNumber

        holderName = (input("enter your name : "))
        self.__holderName = holderName

        balance = int(input("enter your balance: "))
        self.__balance = balance


    def login(self,pin):
        if self.__pin == pin:
            print("Your Pin is correct")
            self.__login = True
        else:
            print("Your pin is incorrect")
            self.__login = False
        
    def get_balance(self):
        print(f" balance : {self.__balance}")

    
    def deposit(self,amount):
        if self.__login:
            self.__balance+=amount
            print("Amount Added")
        else:
            print("Login first please")

    def withdrawal(self,amount):
        if self.__login:
            if self.__balance<amount:
                return print("Insuffiecnt Balance")
            self.__balance-=amount
            print("Withdrawal Success")
        else:
            print("Login First pleasse")

    
    def display(self):
        print(f"AccountNo : {self.__accountNumber}\nBalance : {self.__balance}")


bank = BankAccount("1122","4500",2000)
bank.login("4500")
bank.deposit(1000)
bank.display()
bank.withdrawal(500)
bank.display()
