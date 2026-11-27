# 18. Report Card Generator
# Problem Statement

# Different grading systems exist.

# Create:

# abstract class Student

# Child:

# SchoolStudent
# CollegeStudent

from abc import ABC,abstractmethod

class Student(ABC):

    @abstractmethod
    def grade(self):
        pass


class SchoolStudent(Student):

    def __init__(self,name,marks,total_sub):
        self.__name = name
        self.__marks = marks
        self.__total_sub = total_sub


    def grade(self):
        print("Your School Grade")
        print(f"Name : {self.__name}")
        print(f"{self.__marks/self.__total_sub}%")


class CollegeStudent(Student):

    def __init__(self,name,marks,total_sub):
        self.__name = name
        self.__marks = marks
        self.__total_sub = total_sub


    def grade(self):
        print("Your College Grade")
        print(f"Name : {self.__name}")
        print(f"{(self.__marks/self.__total_sub)/10} SGPA")

c = CollegeStudent("Rudraksh",350,5)
c.grade()
