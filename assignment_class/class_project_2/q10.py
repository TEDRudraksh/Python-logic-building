# 10. Company Department System
# Problem

# Create:

# Department
# Employee

# classes.

# Requirements

# Each department:

# has department name
# stores employee objects
# Functionalities
# Add employee to department
# Display all employees
# Calculate total department salary
# Concepts Practiced
# object composition
# object interaction
# storing objects in lists


class Department:
    def __init__(self, dept_name):
        self.__dept_name = dept_name
        self.__lst = []

    def add(self, obj):
        self.__lst.append(obj)
        print("Employee added successfully!")

    def display(self):
        for emp in self.__lst:
            emp.display()

    def total_salary(self):
        total = 0

        for emp in self.__lst:
            total += emp.get_salary()

        print("Total Department Salary:", total)


class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def display(self):
        print("Name:", self.__name)
        print("Salary:", self.__salary)

    def get_salary(self):
        return self.__salary


dep = Department("IT")

emp1 = Employee("Rud", 4500)
emp2 = Employee("Rahul", 5500)
emp3 = Employee("Aman", 6000)
dep.add(emp1)
dep.add(emp2)
dep.add(emp3)
dep.display()
dep.total_salary()