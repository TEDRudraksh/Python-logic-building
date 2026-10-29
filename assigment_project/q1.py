# 1. Smart Calculator
# Beginner
# Concepts: if-elif-else, while, functions
# Requirements
#     • Display a menu for addition, subtraction, multiplication, division, and modulus.
#     • Take two numbers from the user.
#     • Use separate functions for each operation.
#     • Handle division by zero.
#     • Repeat until the user selects Exit.
# Bonus: Add power and floor division operations.


def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b==0:
        return "cannot divide by 0"
    else:
        return a/b

def module(a,b):
    if b==0:
        return "cannot module by 0"
    else:
        return a%b


def simple_calculator():
   
    while True:
            print("----------Simple Calculator-------------")
            num1 = int(input("enter the 1st number : "))
            num2 = int(input("enter the 2st number : "))
            num =  int(input("what operation you want to do?\nEnter 1 for addition\nEnter 2 for subtraction\nEnter 3 for multiplication\nEnter 4 for Division\nEnter 5 for modules\nEnter 6 for Exit\n"))
        
            if num==1:
                print(f"addition = {addition(num1,num2)}")
    
            elif num==2:
                print(f"subtracion = {subtraction(num1,num2)}")
   
            elif num==3:
                print(f"multiplication =  {multiplication(num1,num2)}")

            elif num==4:
                print(f"division = {division(num1,num2)}")
           
            elif num==5:
                print(f"modules = {module(num1,num2)}")
           
            elif num==6:
                break
            else:
                print("Invalid Option")
                break


simple_calculator()
