n=5
for i in range(1,6):
    A=65
    for j in range(1,n+1):
        if i==1 or j==1 or j==n-i+1:
            print(chr(A),end="")
            A+=1
        else:
            print(" ",end="")
            A+=1
    print()

# ABCDE
# A  D
# A C
# AB
# A