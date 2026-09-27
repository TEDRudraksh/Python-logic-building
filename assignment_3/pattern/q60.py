n=5
for i in range(1,6):

    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        if k==1 or k==i or i==5:
            print("X",end="")
        else:
            print("_",end="")
 
    print()

# X
# X X
# X__X
# X____X
# X X X X X
