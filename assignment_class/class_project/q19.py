# 9. Write a program to create a class called "Employee" with a name, salary, and hire date attributes, 
# and a method to calculate years of service.



class Employee:
    def __init__(self,name="",salary=0,start=0,end=0):

        self.__name = name
        self.__salary = salary
        self.__start = start
        self.__end = end


    def set_details(self):

        name = (input("enter your name : "))
        self.__name = name

        salary = int(input("enter your salary : "))
        self.__salary = salary  

        start = int(input("Enter your Starting year(ex-2004) : "))
        if len(str(start))!=4:
            print("Invalid Year")
        else:
            self.__start = start

        end = int(input("Enter your Ending year(ex-2026) : "))
        if len(str(end))!=4 or end<self.__start:
            print("Invalid Year")
        else:
            self.__end = end

    def calculate(self):
        if self.__end>self.__start:
            print(f"Your Service : {self.__end-self.__start} Years")
        else:
            print("Not Valid Year")


service = Employee()
service.set_details()
service.calculate()