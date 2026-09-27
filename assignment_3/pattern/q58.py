n=5
for i in range(1,6):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")
    print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5