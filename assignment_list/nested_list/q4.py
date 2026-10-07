arr = [[1,2,3],
       [8,1,0],
       [3,4,5]]

final=0
index=0
for row in range(len(arr)):
    sum=0
    for col in range(len(arr[row])):
        sum+=arr[row][col]
    if sum>final:
        final = sum
        index = row

print(final,index)

