# 35. Write a java program to implement selection sort algoritm



arr = [6,2,3,1,5,7]

for i in range(len(arr)):
    first = i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[first]:
            first = j

    arr[i],arr[first] = arr[first],arr[i]
print(arr)



arr = [6,2,3,1,5,7]

for i in range(len(arr)):
    first = i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[first]:
            first = j
            
    arr[i],arr[first] = arr[first],arr[i]