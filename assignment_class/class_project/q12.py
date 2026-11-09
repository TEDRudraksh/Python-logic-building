# 2. Write a  program to create a class called "Dog" with a name and breed attribute. 
# Create two instances of the "Dog" class, set their attributes using the constructor and modify the attributes using the setter methods and
#print the updated values.



class Dog:
    def __init__(self,name="",breed=""):
        self.__name = name
        self.__breed = breed


    def set_details(self):
        name = input("Enter Name : ")
        self.__name = name

        breed = input("Enter Breed : ")
        self.__breed = breed

    def display(self):
        print(f"name : {self.__name}, Breed : {self.__breed}") 

dog1 = Dog()
dog1.set_details()
dog1.display()

dog2 = Dog()
dog2.set_details()
dog2.display()