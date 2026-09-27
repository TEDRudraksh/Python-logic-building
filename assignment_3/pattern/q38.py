n=5
for i in range(5,0,-1):
    for j in range(1,n+1):
        if i==5 or j==1 or j==i:
            print(i,end="")
        else:
            print(" ",end="")

    print()
    n=n-1

# 55555
# 4  4
# 3 3
# 22
# 1