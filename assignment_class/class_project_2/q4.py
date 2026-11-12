# 4. Student Grade System
# Problem

# Create a student result management system.

# Requirements

# Each student should have:

# roll number
# name
# marks in 3 subjects
# Functionalities
# Calculate total marks
# Calculate percentage
# Assign grade:
# A → 90+
# B → 75+
# C → 50+
# Fail otherwise
# Track total students
# Concepts Practiced
# instance methods
# conditional logic in classes
# object-based calculations



class Student:

    __totalStudent = 0

    def __init__(self,name="",roll_no=0,subject={}):
        self.__name = name
        self.__roll_no = roll_no
        self.__subject = subject
        self.__total = 0
        self.__percent = 0
        self.__grade = ""
        Student.__totalStudent+=1


    def calculate(self):
        for marks in self.__subject.values():
            self.__total+=marks

        self.__percent = (self.__total)/3
        if self.__percent>=50:
            if self.__percent>=50 and self.__percent<=74:
                self.__grade = "C"

            elif self.__percent>=75 and self.__percent<=89:
                self.__grade = "B"

            elif self.__percent>=90 and self.__percent<=100:
                self.__grade = "A"
        else:
            self.__grade = "F"

    def display(self):
        print(f"Name : {self.__name}\n Roll no : {self.__roll_no}\ntotal marks : {self.__total}\n percent : {self.__percent}\n Grade : {self.__grade}")

    @classmethod
    def student_count(cls):
        print(f"Total student : {cls.__totalStudent}")


stud1 = Student("Rudrksh",1122,{"marks1":50,"marks2":60,"marks3":70})
stud2 = Student()
stud3 = Student()
stud1.calculate()
stud1.display()
Student.student_count()