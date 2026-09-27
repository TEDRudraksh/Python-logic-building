n=5
for i in range(1,6):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,2*i):
        print(k,end="")
    print()

# 1
# 123
# 12345
# 1234567
# 123456789