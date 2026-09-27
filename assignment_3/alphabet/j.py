for i in range(1,6):
    for j in range(1,6):
        if j==3 or i==1 or (i==5 and j<4) or (j==1 and i>2):
            print("*",end="")
        else:
            print(" ",end="")
    print()
