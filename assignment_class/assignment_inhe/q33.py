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

    def turn_on(self):
        print("Fan Turn On")

    def turn_off(self):
        print("Fan Turn Off")


class SmartLight(Device):

    def turn_on(self):
        print("Light Turn On")

    def turn_off(self):
        print("Light Turn Off")


class SmartAC(Device):

    def turn_on(self):
        print("AC Turn On")

    def turn_off(self):
        print("AC Turn Off")


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