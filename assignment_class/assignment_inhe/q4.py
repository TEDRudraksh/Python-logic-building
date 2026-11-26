# 4. Student Management

# Base class Person.

# Derived:

# Student
# Teacher

# Add role-specific methods.

from abc import ABC,abstractmethod

class Person(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def age(self):
        pass

class Student(Person):

    def __init__(self,name,age,attendance):
        self.__name = name
        self.__age = age
        self.__attendance = attendance

    def name(self):
        print(self.__name)

    def age(self):
        print(self.__age)

    def check_attendance(self):
        print(self.__attendance)

class Teacher(Person):

    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        self.__lst = {"10AM":"English[B]","11AM": "Maths[A]"}

    def name(self):
        print(self.__name)

    def age(self):
        print(self.__age)

    def view_timetable(self):
        print(self.__lst)
        

t = Teacher("R",10)
t.view_timetable()
t.age()
t.name()