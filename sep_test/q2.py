# Q2. Simple Calculator — match-case

# Write a Python program that accepts:

# Two numbers
# An operator (+, -, *, /, %)

# Use match-case to perform the selected operation.

# The program should also handle division by zero.

# Example:

# Enter first number: 20
# Enter second number: 5
# Enter operator: /

# Result: 4.0
num1 = float(input("enter the 1st number : "))
num2 = float(input("enter the 2nd number : "))
operator = input("enter operator (+, -, *, /, %) : ")


match operator:
    case "+":
        print(f"{num1+num2}")
    case "-":
        print(f"{num1-num2}")
    case "*":
            print(f"{num1*num2}")
    case "/":
        if num2!=0:
            print(f"{num1/num2}")
        else:
            print("Cannot divide with 0")
    case "%":
        if num2!=0:
            print(f"{num1%num2}")
        else:
            print("cannot divide with 0")
    case _:
        print("Invalid operator")
    



