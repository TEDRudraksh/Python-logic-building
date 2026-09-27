for i in range(1,6):
    A=65
    for j in range(1,i+1):
        if j==1 or i==5 or i==j:
            print(chr(A),end="")
            A+=1
        else:
            print(" ",end="")
            A+=1
    print()

# A
# AB
# A C
# A  D
# ABCDE