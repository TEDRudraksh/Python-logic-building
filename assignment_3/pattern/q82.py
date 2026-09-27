n=5
for i in range(1,5):
    for k in range(n-i):
        print(" ",end="")
    for j in range(1,2*i):
            if j==1 or j==2*i-1:     
                print("*",end="")
            else:
                 print("_",end="")
    print()

for i in range(3,0,-1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(1,2*i):
            if j==1 or j==2*i-1:     
                print("*",end="")
            else:
                 print("_",end="")
    print()

# *
# *_*
# *___*
# *_____*
# *___*
# *_*
# *