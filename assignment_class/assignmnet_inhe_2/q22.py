# 22. Notification Service
# Problem Statement

# Application sends notifications differently.

# Create:

# abstract class Notification

# Child:

# EmailNotification
# SMSNotification
# PushNotification



from abc import ABC,abstractmethod

class Notification(ABC):
    @abstractmethod
    def notification_call(self):
        pass


class EmailNotification(Notification):
    def notification_call(self):
        print(f"notification_call : Email")


class SMSNotification(Notification):
    def notification_call(self):
        print(f"notification_call : SMS")


class PushNotification(Notification):
    def notification_call(self):
        print(f"notification_call : PUSH")

print("1 for Email Notification")
print("2 for SMS Notification")
print("3 for Push Notification\nEnter choice : ")
choice = int(input())
mode = None
if choice == 1:
    mode = EmailNotification()
    
elif choice == 2:
    mode = SMSNotification()
    
elif choice == 3:
    mode = PushNotification()

mode.notification_call()