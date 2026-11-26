
# 28. Authentication System

# Abstract:

# Authentication

# Derived:

# OTPAuth
# GoogleAuth
# FacebookAuth
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

class FacebookAuth(Authentication):

    __database = [{"username":"1234@","password":"1234"}]

    def auth(self):
        username = input("Enter your Fb Id")
        password = input("Enter your Password")

        for i in FacebookAuth.__database:
            if i["username"]==username and i["password"]==password:
                    print("Auth Sucess")

            else:
                print("Wrong Credentials")

f = FacebookAuth()
f.auth()