# Employee Record System
# Create a class Employee with private fields: id, name, and salary.
# Use setter methods to assign values. Add a method to display employee details.

class Employee:
    def __init__(self,id,name,salary):
        self.__id = id
        self.__name = name
        self.__salary = salary

    def set_details(self):
        id = int(input("enter your id : "))
        self.__id = id

        name = (input("enter your name : "))
        self.__name = name

        salary = int(input("enter your salary : "))
        self.__salary = salary

    def get_details(self):
        print("Employee Details")
        print(f" id : {self.__id}")
        print(f" Name : {self.__name}")
        print(f" salary : {self.__salary}")


EMP = Employee(None, None,None)
EMP.set_details()
EMP.get_details()