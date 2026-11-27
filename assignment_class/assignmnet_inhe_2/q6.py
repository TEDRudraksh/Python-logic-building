# 6. Exam Evaluation System
# Problem Statement

# Marks are evaluated differently.

# Create:

# abstract class Exam

# Child:

# MCQExam
# PracticalExam
# VivaExam

# Each calculates grades differently.


from abc import ABC,abstractmethod

class Exam(ABC):

    def grade(self):
        pass


class MCQExam(ABC):

    def __init__(self,correct,wrong):
        self.__correct = correct
        self.__wrong = wrong
        self.__total = 0

    def grade(self):
        print("Your Grade")
        self.__total = (self.__correct*5) - (self.__wrong*1)
        print(self.__total)


class PracticalExam(ABC):

    def __init__(self,total,sub):
        self.__total = total
        self.__sub = sub


    def grade(self):
        print("Your Grade")
        print(f"{self.__total/self.__sub}%")


class VivaExam(ABC):

    def __init__(self,correct,wrong):
        self.__correct = correct
        self.__wrong = wrong

    def grade(self):
        print("Your Grade")
        print(f"{(self.__correct)}0%")


v = VivaExam(4,5)
v.grade()
