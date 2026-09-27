n=5
for i in range(5,0,-1):
    A=65
    for j in range(i-1):
        print(" ",end="")
    for k in range(n-i+1):
        print(chr(A),end="")
        A+=1
    print()


# A
# AB
# ABC
# ABCD
# ABCDE
