n = 11
count=0
for i in range(2,(n//2)+1):
    if n%i==0:
        count=0
        break
    else:
        count=1
if count or n==2:
    print("prime")
else :
    print("not prime")
