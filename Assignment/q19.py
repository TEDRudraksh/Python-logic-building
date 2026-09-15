num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
choice = input("Enter choice (+, >, ==): ")

if choice == '+':
    print(f"Addition is {num1 + num2}")

elif choice == '>':
    if num1 > num2:
        print("First number is greater")
    elif num2 > num1:
        print("Second number is greater")
    else:
        print("Both numbers are equal")

elif choice == '==':
    if num1 == num2:
        print("Both numbers are equal")
    else:
        print("Both numbers are not equal")

else:
    print("Invalid choice")
