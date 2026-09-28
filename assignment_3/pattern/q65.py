for i in range(5):
    for j in range(5,-1,-1):
        if j>i:
            print(" ",end="")
        else:
            if i==j:
                print(11**i,end="")
    print()