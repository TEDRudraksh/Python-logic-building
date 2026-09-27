n = 6

for i in range(1, 7):
    if i % 2 == 0:
        for j in range(n, 0, -1):
            print(j, end="")
    else:
        for j in range(1, n + 1):
            print(j, end="")

    print()
    n = n - 1


# 123456
# 54321
# 1234
# 321
# 12
# 1