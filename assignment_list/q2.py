arr = [5,2,3,4,6,8]

max = arr[0]
min = arr[0]

for i in range(len(arr)):
    if arr[i]>max:
        max = arr[i]
    elif arr[i]<min:  
        min = arr[i]
print(max,min)