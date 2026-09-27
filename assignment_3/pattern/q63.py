n=5
for i in range(1,6):
    A=65
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,2*i):
        print(chr(A),end="")
        A+=1
    print()


# A
# ABC
# ABCDE
# ABCDEEF
# ABCDEFGHI