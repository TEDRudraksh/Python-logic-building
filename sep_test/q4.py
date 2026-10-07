# Q4. Prime Numbers in a Range — Nested Loops

# Write a Python program that accepts two numbers start and end and prints all prime numbers between them.

# Also display the total number of prime numbers found.

# Example:

# Enter start: 10
# Enter end: 30

# Prime numbers:
# 11 13 17 19 23 29

# Total prime numbers: 6

# Restriction: Do not use any built-in function/library for checking whether a number is prime.


start = int(input("starting number"))
end = int(input("ending number"))
count=0

for n in range(start, end + 1):
    if n < 2:
        continue

    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n,end=" ")
        count += 1
        
print(count)
