
# 1. Write a python program to create a class called "Person" with a name and age attribute. 
# Create two instances of the "Person" class, set their attributes using the constructor, and print their name and age.

class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def display(self):
        print(f" name : {self.__name} age : {self.__age}")


pers1 = Person("Rahul",25)
pers1.display()
pers2 = Person("Rohit",30)
pers2.display()
