n=5
A=69
for i in range(5,0,-1):
    for j in range(1,n+1):
        print(chr(A),end="")
    print()
    n-=1
    A-=1

# EEEEE
# DDDD
# CCC
# BB
# A