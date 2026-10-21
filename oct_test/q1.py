# Q1. If-Else — Number Classification (5 Marks)

# Write a program that accepts an integer and checks whether it is a Harshad number.

# A number is a Harshad number if it is divisible by the sum of its digits.

# Example:

# Input: 18

# Output: Harshad Number (18 is divisible by 1 + 8 = 9)

num = int(input("enter the number"))
sum = 0
temp = num 

while temp:
    n = temp%10
    sum = sum +n
    temp = temp//10

if num%sum==0:
    print("divisible")
else:
    print("not divisible")