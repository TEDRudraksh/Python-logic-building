a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

for n in range(a, b + 1):
    print("Factors of", n)

    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

    print()