# 6. Write a  program to create a class called "Employee" with a name, job title, and salary attributes, 
# and methods to calculate and update salary.


class Employee:
    def __init__(self,job="",name="",basesalary=0,actualsalary=0,allowences=0):
        self.__job = job
        self.__name = name
        self.__basesalary = basesalary
        self.__allowences = allowences
        self.__actualsalary = actualsalary

    def set_details(self):
        name = (input("enter your name : "))
        self.__name = name

        job = (input("enter your job title : "))
        self.__job = job

        salary = int(input("enter your basesalary : "))
        self.__basesalary = salary

        allowences = int(input("enter your allowences amount : "))
        self.__allowences = allowences


    def calculate(self):
        self.__actualsalary = self.__basesalary+self.__allowences
        print(f"Salary : {self.__actualsalary}")
        
        
    def update(self):
        change = int(input("Enter New Base Salary"))
        self.__basesalary = change
        self.__actualsalary = self.__basesalary+self.__allowences

    def get_details(self):
        print("Employee Details")
        print(f"Job Title : {self.__job}")
        print(f"Name : {self.__name }")
        print(f"BaseSalary : {self.__basesalary}")
        print(f"ActualSalary  (base and allowences) : {self.__actualsalary}")



EMP = Employee()
EMP.set_details()
EMP.calculate()
EMP.get_details()
EMP.update()
EMP.get_details()