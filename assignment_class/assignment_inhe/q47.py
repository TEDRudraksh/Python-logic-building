# 47. School ERP System

# Features:

# attendance
# exams
# student records
# teacher management


student = []
teacher = []
class School:

    def __init__(self,name):
        self.__name = name

    def add_student(self,obj):
        student.append(obj)
        print("Student added")
        
    def add_teacher(self,obj):
        teacher.append(obj)
        print("Teacher Added")

    def display_s(self):
        for i in student:
            i.display_student()

    def display_t(self):
        for i in teacher:
            i.display_teacher()

class Student:

    def __init__(self,sname,age,attendance):
        self.__sname = sname
        self.__age = age
        self.__attendance = attendance

    def view_attendance(self):
        print("Attedance")
        print(self.__attendance)

    def display_student(self):
        print(f"name:{self.__sname}")
        print(f"Age: {self.__age}")


class Teacher:

    def __init__(self, tname, subject, salary):
        self.__tname = tname
        self.__subject = subject
        self.__salary = salary

    def display_teacher(self):
        print("Teacher Name:", self.__tname)
        print("Subject:", self.__subject)
        print("Salary:", self.__salary)


class Exam:

    def __init__(self, exam_name):
        self.__exam_name = exam_name
        self.__marks = {}

    def add_marks(self, obj, marks):

        if marks < 0 or marks > 100:
            print("Invalid marks")
            return

        self.__marks[obj] = marks
        print("Marks added successfully")

    def calculate_result(self, obj):

        if obj not in self.__marks:
            print("Student marks not found")
            return

        marks = self.__marks[obj]

        print("\n--- Examination Result ---")
        print("Marks:", marks)
        print("Percentage:", marks, "%")

        

school = School("ABC School")

s1 = Student("Rahul",18,28)
s2 = Student("Amit",19,18)


t1 = Teacher("Rohit", "Python", 40000)
t2 = Teacher("Aman", "Java", 45000)


school.add_student(s1)
school.add_student(s2)


school.add_teacher(t1)
school.add_teacher(t2)


s1.view_attendance()
s2.view_attendance()

exam1 = Exam("Final Examination")


exam1.add_marks(s1, 85)
exam1.add_marks(s2, 92)


exam1.calculate_result(s1)
exam1.calculate_result(s2)


school.display_s()
school.display_t()

