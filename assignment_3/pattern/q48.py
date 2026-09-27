n=5
for i in range(1,6):
    A=65
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        if j==1 or i==5 or j==i:
            print(chr(A),end="")
            A+=1
        else:
            print("_",end="")
            A+=1
    print()


# A
# AB
# A_C
# A__D
# ABCDE
