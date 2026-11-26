
# 12. University System
# Person
# Student(Person)
# GraduateStudent(Student)

# Add thesis information.


class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def name(self):
        return self.__name

    def age(self):
        return self.__age

class Student(Person):
    def __init__(self, name, age,rollno,major):
        super().__init__(name, age)
        self.__rollno = rollno
        self.__major = major



    def details(self):
        print(f"Name : {Person.name(self)}\nAge : {Person.age(self)}\nRollno : {self.__rollno}\nMajor : {self.__major}")

class GradudateStudent(Student):
    def __init__(self, name, age, rollno, major):
        super().__init__(name, age, rollno, major)
        self.__thesis = ""


    def add_thesis(self,thesis):
        self.__thesis = thesis
        print("Thesis Added")

    def display(self):
        print(self.__thesis)


g = GradudateStudent("Rud",25,1122,"CS")
g.details()
g.add_thesis("hello this is thesis info")
g.display()