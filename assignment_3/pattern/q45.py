n=5
for i in range(5,0,-1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(n-i+1):
        print(i,end="")
    print()

# 5
# 44
# 333
# 2222
# 11111
