#instance method

class Message:
    def __init__(self,name,reciever,msg):
        self.name = name
        self.reciever = reciever
        self.msg = msg


    def display(self):
        print(f"Message send by {self.name} msg : {self.msg} Message receive by {self.reciever}")


obj = Message("Rudraksh","Kashish","hello kashish how are you?")
obj.display()
