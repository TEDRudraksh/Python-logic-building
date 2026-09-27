n=8
for i in range(1,8):
    for j in range(1,8):
        if i==j and i<=3 or j==n-i and j>3:
            print("*",end="")
        else:
            print(" ",end="")
    print()