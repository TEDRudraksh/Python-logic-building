# 36. Payment Interface

# Methods:

# pay()

# Implement:

# PayPal
# Stripe
# Razorpay


from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass


class PayPal(Payment):
    def pay(self,payment):
        print(f"Payment using PayPal : {payment}")


class Stripe(Payment):
    def pay(self,payment):
        print(f"Payment using Stripe : {payment}")


class Razorpay(Payment):
    def pay(self,payment):
        print(f"Payment using Razorpay  : {payment}")


print("1 for using PayPal")
print("2 for using Stripe")
print("3 for Razorpay \nEnter choice : ")
choice = int(input())
pay = None
if choice == 1:
    pay = PayPal()
    
elif choice == 2:
    pay = Stripe()
    
elif choice == 3:
    pay = Razorpay()

pay.pay(5000)