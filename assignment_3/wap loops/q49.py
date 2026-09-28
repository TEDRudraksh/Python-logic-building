a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

for n in range(a, b + 1):

    s = 0

    for i in range(1, n):
        if n % i == 0:
            s = s + i

    if s == n:
        print(n, end=" ")