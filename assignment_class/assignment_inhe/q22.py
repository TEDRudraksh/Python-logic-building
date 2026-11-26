# 22. Payment Gateway

# Abstract class Payment.

# Derived:

# CreditCard
# UPI
# Wallet

# Implement payment processing.


from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def payment(self):
        pass


class Wallet(Payment):
    def payment(self,payment):
        print(f"Payment using NetBanking : {payment}")


class UPI(Payment):
    def payment(self,payment):
        print(f"Payment using UPI : {payment}")


class CreditCard(Payment):
    def payment(self,payment):
        print(f"Payment using Credit Card : {payment}")


print("1 for using NetBanking")
print("2 for using UPI")
print("3 for Credit card\nEnter choice : ")
choice = int(input())
pay = None
if choice == 1:
    pay = Wallet()
    
elif choice == 2:
    pay = UPI()
    
elif choice == 3:
    pay = CreditCard()

pay.payment(5000)