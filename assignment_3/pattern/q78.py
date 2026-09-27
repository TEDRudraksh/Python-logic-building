n=5
for i in range(1,5):
    for k in range(1,n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    print()
for i in range(3,0,-1):
    for k in range(1,n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    print()

# 1
# 12
# 123
# 1234
# 123
# 12
# 1