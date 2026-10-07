arr = [2,3,1,4,1,5,6,7,8,2]
result = []

for i in arr:
    if i in result:
        print(i)
        break
    else:
        result.append(i)
else:
    print("no element")