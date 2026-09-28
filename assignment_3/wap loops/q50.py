a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

for n in range(a, b + 1):

    temp = n
    rev = 0

    while temp != 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10

    if n == rev:
        print(n, end=" ")