
for i in range(1,6):
    for j in range(1,6):
        if j==1 or (i==j and i>2) or ((i+j)%2==0 and i<3 and j>3) :
            print("*",end="")
        else:
            print(" ",end="")
    print()
