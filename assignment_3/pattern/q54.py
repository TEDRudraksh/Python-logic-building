n=5
for i in range(1,6):
    A=65
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,n+1):
        if i ==1 or k == n or k==1:
            print(chr(A),end="")
            A+=1
        else:
            print("_",end="")
            A+=1
    print()
    n-=1

# ABCDE
# A__D
# A_C
# AB
# A