arr = [[1,2,3],
       [8,1,0],
       [3,4,5]]

for row in range(len(arr)):
    for col in range(len(arr[row])):
        if row+col==2:
            print(arr[row][col],end=" ")
