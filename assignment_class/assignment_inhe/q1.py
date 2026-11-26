# 1. Animal Sound System

# Create parent class Animal and child classes:

# Dog
# Cat
# Cow

# Override sound() method.

from abc import ABC,abstractmethod
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")

class Cat(Animal):

    def sound(self):
        print("Meoww")

class Cow(Animal):

    def sound(self):
        print("Moooo")        


c = Cow()
c.sound()
