for i in range(1,6):
    for j in range(1,6):
        if j==1 or i ==1 or i == 5 or (j==5 and i>2) or (i==3 and j>2):
            print("*",end="")
        else:
            print(" ",end="")
    print()
