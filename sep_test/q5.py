# Q5. Student Result Menu — match-case + loops + if-else

# Write a menu-driven Python program for managing the result of N students.

# The program should repeatedly display:

# 1. Enter student marks
# 2. Display average marks
# 3. Display highest marks
# 4. Display lowest marks
# 5. Display result
# 6. Exit

# Use match-case for menu selection.

# For each student, marks are entered for:

# Python
# Database
# Programming

# A student passes only if:

# Marks in each subject >= 40
# Overall percentage >= 50

# For the Display Result option, print:

# Student 1: Pass
# Student 2: Fail
# Student 3: Pass

# The menu should continue until the user selects 6. Exit.

while True:
    marks1 = int(input("enter python marks"))
    marks2 = int(input("enter database marks"))
    marks3 = int(input("enter programming marks"))
    avrage = (marks1+marks2+marks3)/3
    high = 0 
    low = 0
    passed = ""

    if marks1>marks2 and marks1 > marks3:
        high = marks1
    elif marks2>marks3 and marks2>marks1:
        high = marks2
    else:
        high = marks3
    if marks1<marks2 and marks1<marks3:
        low = marks1
    elif marks2<marks3 and marks2<marks1:
        low = marks2
    else:
        low = marks3

    if marks1>40 and marks2>40 and marks3>40 and avrage>=40:
        passed = "pass"
    else:
        passed = "fail"



    marks = int(input("enter your choice"))
    match marks:
        case 1:
            print(avrage)
        case 2:
            print(high)
        case 3:
            print(low)
        case 4:
            print(passed)
        case 5:
            break
        case _ :
            print("invalid")



