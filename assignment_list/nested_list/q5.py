arr = [[1,2,3],
       [8,1,0],
       [3,4,5]]

high = 0
low = 0
h1=0
l1=0
for row in range(len(arr)):
    sum=0
    for col in range(len(arr[row])):
        sum+=arr[row][col]
    if row == 0:
        high = sum
        low = sum
    if sum>high:
        high = sum
        h1 = row
    if sum<low:
        low = sum
        l1 = row

arr[l1],arr[h1] = arr[h1],arr[l1]

print(arr)

