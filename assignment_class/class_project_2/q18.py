# 18. School Classroom System
# Problem

# Create classroom system.

# Requirements

# Classroom should:

# maintain student objects
# maintain class teacher
# Functionalities
# Add student
# Remove student
# Display class strength
# Concepts Practiced
# object aggregation
# collections of objects


class Classroom:
    __lst = []
    __teacher = []

    def add_student(self,obj):
        self.__lst.append(obj)
        print("Student Added")

    def remove_student(self,obj):
        self.__lst.remove(obj)
        print("Student Removed")  

    def add_teacher(self,obj):
        self.__teacher.append(obj)
        print("Teacher Added")

    def remove_teacher(self,obj):
        self.__teacher.remove(obj)
        print("Teacher Removed")    

    def display(self):
        print("Student Number")
        print(len(self.__lst))

        print("Teacher Number")
        print(len(self.__teacher))

class Stundet:
    def __init__(self,name,sid):
        self.__name = name
        self.__sid = sid

class Teacher:
    def __init__(self,name,tid):
        self.__name = name
        self.__tid = tid



stud1 = Stundet("r",33)
stud2 = Stundet("u",44)
stud3 = Stundet("d",55)

tech = Teacher("y",99)

cls = Classroom()
cls.add_teacher(tech)
cls.add_student(stud1)
cls.display()
cls.add_student(stud2)
cls.display()
cls.remove_student(stud1)
cls.display()
