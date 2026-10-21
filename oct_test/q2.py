
# Q2. Loops — Prime Numbers (5 Marks)

# Write a program to print all prime numbers between 1 and 100. Do not use any built-in prime-checking function.

# Expected output: 2, 3, 5, 7, 11, ... 97




for n in range(2,101):
    prime=True
    for p in range(2,n):
        if n%p==0:
            prime = False
            break
    if prime:
        print(n)