#static method

class Message:
    
    def m1(self): # self :-  Refere current object
        print("Instance method")

    @staticmethod
    def m2():
        print("Class method...")
    
obj = Message()
obj.m1()
Message.m2()