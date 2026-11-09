# 10. Write a program to create a class called "Student" with a name, grade, 
# and courses attributes, and methods to add and remove courses.

class Student:
    def __init__(self,name="",grade="",courses=[]):
        self.__name = name
        self.__grade = grade
        self.__courses = courses


    def add_courses(self):
        course = input("Add Your Course : ")
        self.__courses.append(course)
        print("Course Added")


    def remove_courses(self):
        course = input("Course To Remove : ")
        if course in self.__courses:         
            self.__courses.remove(course)
            print("Course Removed")
        else:
            print("Course Not Found")


    def display(self):
        print(f"Corses : {self.__courses}")

stud = Student("Rudraksh","A",["Python","Computer","Data","English"])
stud.display()
stud.add_courses()
stud.display()
stud.remove_courses()
stud.display()
