n=5
for i in range(1,6):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,2*i):
        if i==k and (i+k)%2==0:
            print("#",end="")
        else:
            print("*",end="")
    print()

#    #
#   *#*
#  **#**
# ***#***
#****#****