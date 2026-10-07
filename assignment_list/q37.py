arr = [5,2,3,1,6,8]

for i in range(len(arr)):
    j = i

    while j>0 and arr[j]<arr[j-1]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        j -= 1

print(arr)



arr = [5,2,3,1,6,8]

for i in range(1,len(arr)):
    j=i
    while j>0 and arr[j]<arr[j-1]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        j-=1
