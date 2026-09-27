n=5
for i in range(1,6):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        if j==1 or i==5 or j==i:
            print("1",end="")
        else:
            print("*",end="")
    print()

# 1
# 11
# 1*1
# 1**1
# 11111
