# Q3. Number Analysis — Loop + if-else

# Write a Python program that accepts a positive integer N and prints:

# Sum of all digits
# Number of digits
# Largest digit
# Smallest digit
# Whether the number is a palindrome

# Example:

# Enter number: 12321

# Sum of digits: 9
# Number of digits: 5
# Largest digit: 3
# Smallest digit: 1
# Palindrome: Yes

# Restriction: Do not convert the number into a string.

number = int(input("enter the number"))

n = number
original = n

sum = 0
count = 0
largest = 0
smallest = 0
rev = 0 
while number>0:
    last = number % 10
    sum += last
    number = number//10
    count +=1

    if last > largest:
        largest = last
    else:
        smallest = last
    rev = rev * 10 + last
    if rev==original:
        ok = "yes"
    else:
        ok = "no"
      



print(sum)
print(count)
print(smallest)
print(largest)
print(ok)



