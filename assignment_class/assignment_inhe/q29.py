# 29. Employee Attendance

# Abstract:

# Employee

# Derived:

# FullTimeEmployee
# PartTimeEmployee

# Calculate working hours.

from abc import ABC,abstractmethod
class Employee(ABC):

    @abstractmethod
    def hour_worked(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(self):
        self.__hour = 0

    def hour_worked(self):
        days = int(input("Enter days you worked"))
        print("Total Hours Worked By You as FullTime")
        self.__hour = days*8
        print(self.__hour)



class PartTimeEmployee(Employee):

    def __init__(self):
        self.__hour = 0

    def hour_worked(self):
        days = int(input("Enter days you worked"))
        print("Total Hours Worked By You as PartTime")
        self.__hour = days*4
        print(self.__hour)


p = PartTimeEmployee()
f = FullTimeEmployee()

p.hour_worked()
f.hour_worked()