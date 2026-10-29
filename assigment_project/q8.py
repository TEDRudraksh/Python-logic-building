# 8. Employee Attendance and Salary Calculator
# Intermediate
# Concepts: Conditions, loops, functions, dictionaries
# Requirements
#     • Enter employee details and days present.
#     • Calculate attendance percentage.
#     • Calculate salary based on days worked.
#     • Apply a bonus or deduction according to attendance rules.
#     • Generate an employee summary.

def attdendance(a):
    fix = 26
    percent = (a/fix)*100
    return percent 

def salary_cal(s,a):
    fix = 26
    day = (s/fix)
    salary = day*a
    return salary

def summary():
    name = input("Enter Your Name : ")
    salary = float(input("Enter Your Salary : "))
    attdendance_come = int(input("Enter how many day you come : "))
    percent = attdendance(attdendance_come)
    salary_amount = salary_cal(salary,attdendance_come)
    print(name)
    print(f"Percentage : {round(percent)}")
    print(f"Salary : {round(salary_amount)}")


summary()