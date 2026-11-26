# 33. Smart Home Devices

# Methods:

# turn_on()
# turn_off()

# Implement:

# SmartFan
# SmartLight
# SmartAC

from abc import ABC,abstractmethod

class Device(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class SmartFan(Device):

    def __init__(self):
        self.__on = False
        self.__off = True

    def turn_on(self):
        if self.__off:
            print("Fan put on")
            self.__on = True
            self.__off = False
            
        else:
            print("Fan is Already on")

    def turn_off(self):
        if self.__on:
            print("Fan turn off")
            self.__off = True

        else:
            print("Fan is Already off")


class SmartLight(Device):

    def __init__(self):
        self.__on = False
        self.__off = True

    def turn_on(self):
        if self.__off:
            print("Light put on")
            self.__on = True
            self.__off = False
            
        else:
            print("Light is Already on")

    def turn_off(self):
        if self.__on:
            print("Light turn off")
            self.__off = True

        else:
            print("Light is Already off")


class SmartAC(Device):

    def __init__(self):
        self.__on = False
        self.__off = True

    def turn_on(self):
        if self.__off:
            print("AC put on")
            self.__on = True
            self.__off = False
            
        else:
            print("AC is Already on")

    def turn_off(self):
        if self.__on:
            print("AC turn off")
            self.__off = True

        else:
            print("AC is Already off")

print("1 for SmartFan")
print("2 for SmartLight")
print("3 for SmartAC\nEnter choice : ")
choice = int(input())
op = None
if choice == 1:
    op = SmartFan()
    
elif choice == 2:
    op = SmartLight()
    
elif choice == 3:
    op = SmartAC()

op.turn_on()
op.turn_off()