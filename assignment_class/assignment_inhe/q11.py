# 11. Company Hierarchy
# Person
# Employee(Person)
# Manager(Employee)

# Display company hierarchy.

class Person:
    def __init__(self):
        print("Person")

class Employee(Person):
    def __init__(self):
        super().__init__()
        print("Employee")

class Manager(Employee):
    def __init__(self):
        super().__init__()
        print("Manager")


m = Manager()
