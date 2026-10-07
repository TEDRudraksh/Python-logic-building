arr = [5,8,3,4,10]
n=2
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j] = arr[j],arr[i]

print(arr)
print(f"{arr[n-1],arr[len(arr)-n]}")
