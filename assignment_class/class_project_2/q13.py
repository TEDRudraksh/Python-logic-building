# 13. Exam Portal
# Problem

# Create exam management system.

# Requirements

# Each exam object:

# exam name
# total marks
# passing marks
# Functionalities
# Check pass/fail
# Calculate grade
# Maintain total exams conducted

class Exam:
    __count = 0

    def __init__(self,name,marks,passMarks):
        self.__name = name
        self.__marks = marks
        self.__passMarks = passMarks
        Exam.__count+=1

    def check(self):
        if self.__marks>=self.__passMarks:
            print("Pass in Exam")
            return  True
        else:
            print("Fail in Exam")
            return False

    def grade(self):
        if self.check():
            if self.__marks>=90:
                print("A")
            elif self.__marks>=75 and self.__marks<90:
                print('B')
            elif self.__marks>=50 and self.__marks<75:
                print("C")
            else:
                print("D")
        else:
            print("Fail")
result = Exam("JEE",200,165)
result.check()
result.grade()