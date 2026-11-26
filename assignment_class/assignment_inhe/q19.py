# 19. Mobile Phone Hierarchy
# Phone
# Smartphone
# AndroidPhone

# Add Android features.

class Phone:

    def __init__(self,model,brand):
        self.__model = model
        self.__brand = brand

    def dial_call(self):
        print("Calling")

    def recive_call(self):
        print("Reciveed called")


class Smartphone(Phone):

    def __init__(self, model, brand, os):
        super().__init__(model, brand)
        self.__os = os

    def camera(self):
        print("photo Clicked")


    def get_os(self):
        return self.__os 


class AndroidPhone(Smartphone):

    def __init__(self, model, brand, os,internet):
        super().__init__(model, brand,os)
        self.__internet = internet


    def google(self):
        if self.__internet:
            print("Your Result : Python is very Simple")
        else:
            print("You dont have access of internet")


a = AndroidPhone("10xx","Samsung","Android",False)
a.dial_call()
a.recive_call()
a.camera()
a.google()


