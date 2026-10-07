arr = [[1,2,3],
       [8,1,0],
       [3,4,5]]


for row in range(len(arr)):
    first = 0
    last = len(arr[row])-1

    while first<last:
        arr[row][first], arr[row][last] = arr[row][last], arr[row][first]
        first += 1
        last -= 1
print(arr)