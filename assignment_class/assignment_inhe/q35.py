# 35. Messaging Application

# Methods:

# send_message()

# Implement:

# WhatsApp
# Telegram
# Signal

from abc import ABC,abstractmethod


class MessageApplication(ABC):

    @abstractmethod
    def send_messgae(self):
        pass


class Whatsapp(MessageApplication):

    def send_messgae(self):
        print("You are Using Whatsapp")
        to = input("Select Contact (name)")
        msg = input("Enter your message")
        print(f"Message Sent to {to}")


class Telegram(MessageApplication):

    def send_messgae(self):
        print("You are Using Telegram")
        to = input("Select Contact (name)")
        msg = input("Enter your message")
        print(f"Message Sent to {to}")


class Signal(MessageApplication):

    def send_messgae(self):
        print("You are Using Signal")
        to = input("Select Contact (name)")
        msg = input("Enter your message")
        print(f"Message Sent to {to}")



print("1 for Whatsapp")
print("2 for Telegram")
print("3 for Signal\nEnter choice : ")
choice = int(input())
app = None
if choice == 1:
    app = Whatsapp()
    
elif choice == 2:
    app = Telegram()
    
elif choice == 3:
    app= Signal()

app.send_messgae()