n=5
for i in range(1,6):
    for j in range(n+1-i):
        if i%2==0:
            print("#",end="")
        else:
            print("*",end="")

    print()

# *****
# ####
# ***
# ##
# *