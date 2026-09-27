n=5
for i in range(1,5):
    for k in range(n-i):
        print(" ",end="")
    for j in range(1,2*i):
        if j%2==0:
            print("_",end="")
        else:
            print("*",end="")
    print()

for i in range(3,0,-1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(1,2*i):
        if j%2==0:
            print("_",end="")
        else:
            print("*",end="")
    print()


# *
# *_*
# *_*_*
# *_*_*_*
# *_*_*
# *_*
# *