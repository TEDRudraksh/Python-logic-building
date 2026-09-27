n=6
for i in range(1,7):
    for k in range(n-i):
        print(" ",end="")
    for j in range(1,2*i):
        if j%2==0:
            print("0",end="")
        else:
            print("1",end="")
    print()











# 1
# 101
# 10101
# 1010101
# 101010101   
# 10101010101