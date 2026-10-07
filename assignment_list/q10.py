

arr = [10, 20, 40, 30, 20, 60]
k=5
for j in range(k):
    last = arr[-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]

    arr[0] = last
    print(arr)

