n=5
for i in range(1,6):
    for j in range(1,6):
        if i==j and i<3 or j==n-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()