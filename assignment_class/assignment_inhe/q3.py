# 3. Employee Management

# Base class Employee.

# Derived:

# Developer
# Tester
# HR

# Calculate salaries differently.



from abc import ABC,abstractmethod
class Employee(ABC):

    @abstractmethod
    def salary(self):
        pass

class Developer(Employee):

    def __init__(self,Basesalary,bonus):

        self.__Basesalary = Basesalary
        self.__bonus = bonus
        self.__total = 0
    
    def salary(self):
       self.__total = self.__Basesalary + self.__bonus
       print(self.__total)


class Tester(Employee):

    def __init__(self,Basesalary,bonus):

        self.__Basesalary = Basesalary
        self.__bonus = bonus
        self.__total = 0
    
    def salary(self):
       self.__total = self.__Basesalary + self.__bonus
       print(self.__total)


class HR(Employee):

    def __init__(self,Basesalary,bonus):

        self.__Basesalary = Basesalary
        self.__bonus = bonus
        self.__total = 0
    
    def salary(self):
       self.__total = self.__Basesalary + self.__bonus
       print(self.__total)

c = HR(50000,5000)
t = Tester(40000,2000)
d = Developer(60000,6000)
c.salary()
