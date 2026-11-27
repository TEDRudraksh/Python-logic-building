# 12. Authentication System
# Problem Statement

# Users can login using multiple methods.

# Create:

# abstract class Authentication

# Child:

# OTPAuth
# GoogleAuth
# FingerprintAuth




import random 
from abc import ABC,abstractmethod
class Authentication:

    @abstractmethod
    def auth(self):
        pass


class OTPAuth(Authentication):

    def auth(self):
        phone = int(input("Enter No."))
        otp = random.randint(1000,9999)
        print(otp)
        enter = int(input("Enter Otp for authentication"))

        if otp == enter:
            print("Authentication Sucess")
        else:
            print("Wrong OTP")

class GoogleAuth(Authentication):

    def auth(self):
        email = input("Enter your Email")
        code = random.randint(100000,999999)
        print(code)
        enter = int(input("Enter Code for authentication"))

        if code == enter:
            print("Authentication Sucess")
        else:
            print("Wrong Code")


class FingerPrintAuth(Authentication):

    def auth(self):
        print("Press Finger print Scanner")
        print("Authentication Sucess")


print("1 for OTPAuth")
print("2 for GoogleAuth")
print("3 for FingerPrintAuth\nEnter choice : ")
choice = int(input())
auth = None
if choice == 1:
    auth = OTPAuth()
    
elif choice == 2:
    auth = GoogleAuth()
    
elif choice == 3:
    auth= FingerPrintAuth()

auth.auth()


