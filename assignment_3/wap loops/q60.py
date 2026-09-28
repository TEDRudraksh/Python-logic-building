import math

n = int(input("Enter N: "))

for i in range(1, n + 1):
    print("Number =", i)
    print("Square =", i * i)
    print("Cube =", i * i * i)
    print("Square Root =", math.sqrt(i))
    print()