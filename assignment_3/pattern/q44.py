n=5
for i in range(1,6):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(i,end="")
    print()

# 1
# 22
# 333
# 4444
# 55555