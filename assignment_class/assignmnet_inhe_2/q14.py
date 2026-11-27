# 14. Employee Attendance Tracker
# Problem Statement

# Attendance calculation differs.

# Create:

# abstract class Employee

# Child:

# FullTimeEmployee
# PartTimeEmployee
# ContractEmployee



from abc import ABC,abstractmethod
class Employee(ABC):

    @abstractmethod
    def attendance(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(self):

        self.__attendance = 0
        

    def days_worked(self):

        if self.__attendance<=21:
            print(f"You Worked for : {self.__attendance}Days")


    def attendance(self):
        if self.__attendance<=21:
            self.__attendance+=1
            print("Attendance Marked")
        else:
            print("Already Worked for this month")


class PartTimeEmployee(Employee):

    def __init__(self):

        self.__attendance = 0


    def days_worked(self):

        if self.__attendance<=13:
            print(f"You Worked for : {self.__attendance}Days")

    
    def attendance(self):
        if self.__attendance<=13:
            self.__attendance+=1
            print("Attendance Marked")
        else:
            print("Already Worked for this month")


class ContractEmployee(Employee):

    def __init__(self):
        self.__attendance = 0

    def days_worked(self):

        if self.__attendance<=21:
            print(f"You Worked for : {self.__attendance}Days")

    def attendance(self):
        if self.__attendance<=7:
            self.__attendance+=1
            print("Attendance Marked")
        else:
            print("Already Worked for this month")


p = PartTimeEmployee()

p.attendance()
p.attendance()
p.attendance()
p.attendance()
p.attendance()
p.attendance()
p.attendance()
p.attendance()
p.attendance()
p.attendance()
p.attendance()
p.attendance()
p.attendance()
p.attendance()
p.attendance()
p.attendance()
p.attendance()
p.days_worked()

