# 30. Chatbot Reply System
# Problem Statement

# Different bots reply differently.

# Create:

# SupportBot
# SalesBot
# FAQBot


from abc import ABC,abstractmethod

class Chatbot(ABC):

    @abstractmethod
    def query(self):
        pass

    @abstractmethod
    def response(self):
        pass


class SupportBot(Chatbot):

    def query(self):
        print("I am Supprot Bot , how can i help you?")
        choice = input("What is Your Query")

    def response(self):
        print("Thank you your Query is submitted")



class SalesBot(Chatbot):

    def query(self):
        print("I am Sales Bot , how can i help you?")
        choice = input("What is Your Query")
        self.response()

    def response(self):
        print("Thank you your Query is submitted")


class FAQBot(Chatbot):

    def query(self):
        print("I am FAQBot  , how can i help you?")
        choice = input("What is Your Query")
        self.response()

    def response(self):
        print("Thank you your Query is submitted")


f = FAQBot()
f.query()