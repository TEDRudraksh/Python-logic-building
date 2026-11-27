# 17. Smart Appliance Controller
# Problem Statement

# Different appliances behave differently.

# Create:

# abstract class Appliance

# Child:

# Fan
# AC
# WashingMachine

from abc import ABC,abstractmethod

class Appliance(ABC):

    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @abstractmethod
    def operation(self):
        pass


class AC(Appliance):

    def __init__(self):
        self.__on = False
        self.__off = True

    def on(self):
        if self.__off:
            print("AC put on")
            self.__on = True
            self.__off = False
            
        else:
            print("AC is Already on")

    def off(self):
        if self.__on:
            print("AC turn off")
            self.__off = True

        else:
            print("AC is Already off")

    def operation(self):
        if self.__on and not self.__off:
            print("AC is giving cool air")
        else:
            print("AC is Off ,turn on it")


class Fan(Appliance):

    def __init__(self):
        self.__on = False
        self.__off = True

    def on(self):
        if self.__off:
            print("Fan put on")
            self.__on = True
            self.__off = False
            
        else:
            print("Fan is Already on")

    def off(self):
        if self.__on:
            print("Fan turn off")
            self.__off = True

        else:
            print("Fan is Already off")

    def operation(self):
        if self.on() and not self.off():
            print("Fan is giving cool air")
        else:
            print("Fan is Off ,turn on it")


class WashingMachine(Appliance):

    def __init__(self):
        self.__on = False
        self.__off = True

    def on(self):
        if self.__off:
            print("Washing Machine put on")
            self.__on = True
            self.__off = False
            
        else:
            print("Washing Machine is Already on")

    def off(self):
        if self.__on:
            print("Washing Machine turn off")
            self.__off = True

        else:
            print("Washing Machine is Already off")

    def operation(self):
        if self.__on and not self.__off:
            print("Washing Machine is giving cool air")
        else:
            print("Washing Machine is Off ,turn on it")


print("1 for AC")
print("2 for Fan")
print("3 for Washing Machine\nEnter choice : ")
choice = int(input())
op = None
if choice == 1:
    op = AC()
    
elif choice == 2:
    op = Fan()
    
elif choice == 3:
    op = WashingMachine()

op.on()
op.operation()