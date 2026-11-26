# 44. Online Examination System

# Features:

# Student
# Exam
# Result

# Use abstract classes for exams.


from abc import ABC,abstractmethod
class Exam(ABC):

    @abstractmethod
    def Subject(self):
        pass



class Python(Exam):

    def __init__(self,marks):
        self.__marks = marks

    def Subject(self):
        print("Python Exam")

    def get_marks(self):

        return self.__marks

class Student(Python):

    def __init__(self,name,age,marks):
        super().__init__(marks)
        self.__name = name
        self.__age = age


    def display(self):
        print("Details of Student")
        print(f"Name : {self.__name}")
        print(f"Age : {self.__age}")


class Result(Student):

    def __init__(self, name, age, marks):
        super().__init__(name, age, marks)


    def result(self):
        print("Your Result")
        self.display()

        if self.get_marks()>=35:
            print("You passed")
        else:
            print("You Failed")

r = Result("Rudraksh",25,57)
r.result()
