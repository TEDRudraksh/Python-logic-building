marks1= int(input("enter the number  : "))
marks2= int(input("enter the number : "))
marks3= int(input("enter the number : "))

total_marks = (marks1 + marks2 + marks3)/3

if total_marks>80:
    print("A")
elif total_marks>=60 and total_marks<=80:
    print("B")
elif total_marks>=50 and total_marks<60:
    print("C")
elif total_marks>=45 and total_marks<50:
    print("D")
elif total_marks>=25 and total_marks<45:
    print("E")
elif total_marks>25:
    print("F")