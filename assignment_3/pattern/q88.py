n = 5

for i in range(1, 2 * n):
    if i < n:
        print("    " + str(i))

    elif i == n:
        for j in range(1, n + 1):
            print(j, end="")
        for j in range(n - 1, 0, -1):
            print(j, end="")
        print()

    else:
        print("    " + str(2 * n - i))