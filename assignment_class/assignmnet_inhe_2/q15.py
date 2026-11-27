# 15. Payment Processing System
# Problem Statement

# Payment methods process payments differently.

# Create:

# abstract class Payment

# Child:

# CreditCard
# DebitCard
# UPI



from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def payment(self):
        pass


class CreditCard(Payment):
    def payment(self,payment):
        print(f"Payment using CreditCard : {payment}")


class UPI(Payment):
    def payment(self,payment):
        print(f"Payment using UPI : {payment}")


class DebitCard(Payment):
    def payment(self,payment):
        print(f"Payment using Debit Card : {payment}")


print("1 for using DebitCard")
print("2 for using UPI")
print("3 for Credit card\nEnter choice : ")
choice = int(input())
pay = None
if choice == 1:
    pay = DebitCard()
    
elif choice == 2:
    pay = UPI()
    
elif choice == 3:
    pay = CreditCard()

pay.payment(5000)