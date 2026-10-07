arr = [[1,2,3],
       [8,1,0],
       [3,4,5]]


arr = [[1,2,3,5],
       [8,1,0,7],
       [3,4,5,8],
       [5,2,0,4]]

for row in range(len(arr)):
    for col in range(len(arr[row])):
        if col>row:
            arr[col][row],arr[row][col] = arr[row][col],arr[col][row]

print(arr)


