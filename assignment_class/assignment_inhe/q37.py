# 37. Social Login System

# Methods:

# login()

# Implement:

# GoogleLogin
# GitHubLogin
# LinkedInLogin

from abc import ABC,abstractmethod

class LoginSystem(ABC):

    @abstractmethod
    def login(self):
        pass



class GoogleLogin(LoginSystem):


    def __init__(self):
        self.__email = "abc@gmail.com"
        self.__password = "123456"

    
    def login(self):
        print("Login with Google")
        email = input("Enter your email")
        password = input("Enter your Password")

        if self.__email == email and self.__password == password:
            print("Login sucess")

        else:
            print("Invalid password or email")




class GitHubLogin(LoginSystem):


    def __init__(self):
        self.__username = "TEDRudraksh"
        self.__password = "123456"

    
    def login(self):
        print("Login with Github")
        username = input("Enter your username")
        password = input("Enter your Password")

        if self.__username == username and self.__password == password:
            print("Login sucess")

        else:
            print("Invalid password or username")




class LinkedInLogin(LoginSystem):


    def __init__(self):
        self.__email = "abc@gmail.com"
        self.__password = "123456"

    
    def login(self):
        print("Login with LinkedInLogin")
        email = input("Enter your email")
        password = input("Enter your Password")

        if self.__email == email and self.__password == password:
            print("Login sucess")

        else:
            print("Invalid password or email")



print("1 for GoogleLogin")
print("2 for GitHubLogin")
print("3 for LinkedInLogin \nEnter choice : ")
choice = int(input())
access = None
if choice == 1:
    access = GoogleLogin()
    
elif choice == 2:
    access = GitHubLogin()
    
elif choice == 3:
    access = LinkedInLogin()

access.login()