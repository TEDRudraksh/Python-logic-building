n=5
for i in range(1,6):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,n+1):
        print(k,end="")
    print()
    n-=1


# 12345
# 1234
# 123
# 12
# 1