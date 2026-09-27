n=5
for i in range(1,6):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,2*n):
        if k==1 or i==1 or k == 2*n-1:
            print(k,end="")
        else:
            print("+",end="")
            
        

    print()
    n-=1

# 123456789
# 1+++++7
# 1+++5
# 1+3
# 1