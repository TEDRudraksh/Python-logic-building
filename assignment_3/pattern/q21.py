for i in range(1,6):
    for j in range(1,i+1):
        if j==1 or i==5 or i==j:
            print(i,end="")
        else:
            print(" ",end="")
    print()


# 1
# 22
# 3 3
# 4  4
# 55555
