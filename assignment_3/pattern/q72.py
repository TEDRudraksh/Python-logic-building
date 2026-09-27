n=5
for i in range(1,6):
    A=65
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,n+1):
            print(chr(A),end="")
            A+=1
    print()
    n-=1


# A B C D E
# A B C D
# A B C
# A B
# A