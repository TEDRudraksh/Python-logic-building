# 13. Smart Device System
# Device
# SmartDevice(Device)
# SmartTV(SmartDevice)

# Add WiFi support.

class Device:
    def __init__(self,model):
        self.__model = model


    def model(self):
        print(self.__model)


class SmartDevice(Device):

    def __init__(self, model,setupbox):
        super().__init__(model)
        self.__setupbox = setupbox

    def setupbox(self):
        print(self.__setupbox)


class SmartTv(SmartDevice):

    def __init__(self, model, setupbox):
        super().__init__(model, setupbox)
        self.__wifi = False

    def add_wifi(self):
        self.__wifi = True
        print("Wifi Support Added")

s = SmartTv("3344",True)
s.model()
s.setupbox()
s.add_wifi()