n=5
A=65
for i in range(1,6):

    for j in range(n-i):
        print(" ",end="")
    for k in range(1,2*i):
        if k ==1 or k == 2*i-1 or i==5:
            print(chr(A),end="")

        else:
            print(" ",end="")


    print()
    A+=1


# A
# B B
# C  C
# D    D
# EEEEEEEEE