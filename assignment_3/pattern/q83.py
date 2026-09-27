for i in range(1,6):
    for j in range(1,6):
        if i==1 or j==1 or j==5 or i==5:
            print("|",end="")
        elif i==j:
            print("\\",end="")
        elif (i+j)%2==0:
            print("/",end="")
        else:
            print(" ",end="")
    print()


# |||||
# |\ /|
# | \ |
# |/ \|
# |||||