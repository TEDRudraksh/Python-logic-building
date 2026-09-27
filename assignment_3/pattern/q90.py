n=8
for i in range(1,8):
    for j in range(1,8):
        if i==j or j==n-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()