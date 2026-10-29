# 2. Student Result Management System
# Beginner
# Concepts: Conditions, loops, functions
# Requirements
#     • Input marks for five subjects.
#     • Calculate total, percentage, and grade.
#     • Check whether the student passed or failed.
#     • Validate that each mark is between 0 and 100.
#     • Create functions such as calculate_total(), calculate_percentage(), and calculate_grade().
# Bonus: Accept results for multiple students and calculate the class average.


def calculate_total(m1,m2,m3,m4,m5):
    return m1+m2+m3+m4+m5

def calculate_percentage(m1,m2,m3,m4,m5):
    return (m1+m2+m3+m4+m5)/5

def calculate_grade(m1,m2,m3,m4,m5):
        percent = (m1+m2+m3+m4+m5)/5
        if percent>=90:
             return "A"
        elif percent<90 and percent>=75:
             return "B"
        elif percent<75 and percent>=60:
             return "C"
        elif percent<60 and percent>=33:
             return "D"
        

# def student_management():
#         marks1 = float(input("enter number for 1st subject : "))
#         marks2 = float(input("enter number for 2st subject : "))
#         marks3 = float(input("enter number for 3st subject : "))
#         marks4 = float(input("enter number for 4st subject : "))
#         marks5 = float(input("enter number for 5st subject : "))

#         if (0 <= marks1 <= 100 and 0 <= marks2 <= 100 and 0 <= marks3 <= 100 and 0 <= marks4 <= 100 and 0 <= marks5 <= 100):
             
#             while True:  
            
#                 if calculate_percentage(marks1,marks2,marks3,marks4,marks5)>=33:
#                     print("Student Passed")
#                     print(f"Grade = {calculate_grade(marks1,marks2,marks3,marks4,marks5)}")
#                     print(f"total marks = {calculate_total(marks1,marks2,marks3,marks4,marks5)}/500")
#                     print(f"percentage = {calculate_percentage(marks1,marks2,marks3,marks4,marks5)}")
#                     break
#                 else:
#                     print("Student Failed")
#                     print(f"total marks = {calculate_total(marks1,marks2,marks3,marks4,marks5)}/500")
#                     print(f"percentage = {calculate_percentage(marks1,marks2,marks3,marks4,marks5)}")
#                     break
#         else:
#              print("Invalid Marks please check")

# student_management()

def student_management():
        student = int(input("How Many Student Marks you want to enter?"))
        class_marks = 0
  
        for i in range(1,student+1):
            print(f"Student {i} Marks")           
            marks1 = float(input("enter number for 1st subject : "))
            marks2 = float(input("enter number for 2st subject : "))
            marks3 = float(input("enter number for 3st subject : "))
            marks4 = float(input("enter number for 4st subject : "))
            marks5 = float(input("enter number for 5st subject : "))

            if (0 <= marks1 <= 100 and 0 <= marks2 <= 100 and 0 <= marks3 <= 100 and 0 <= marks4 <= 100 and 0 <= marks5 <= 100):

                total = calculate_total(marks1,marks2,marks3,marks4,marks5)
                perentage = calculate_percentage(marks1,marks2,marks3,marks4,marks5)
                grade = calculate_grade(marks1,marks2,marks3,marks4,marks5)

                if perentage>=33:
                    print(f"Student {i} Passed")
                    print(f"Total marks = {total}/500")
                    print(f"Percentage = {perentage}")
                    print(f"Grade = {grade}")
                    print("-------------------------")

                    class_marks+=total
                else:
                    print(f"Student {i} Failed")
                    print(f"Total marks = {total}/500")
                    print(f"Percentage = {perentage}")
                    print("-------------------------")
                    class_marks+=total
            else:
                 print("Not valid marks")
        else:
             print(f"total average marks of class = {class_marks/student}/500")           
                
           
student_management()

     