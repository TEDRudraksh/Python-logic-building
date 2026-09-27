n=5
for i in range(1,6):
    A=65
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(chr(A),end="")
        A+=1
    print()

# A
# A B
# A B C
# A B C D
# A B C D E