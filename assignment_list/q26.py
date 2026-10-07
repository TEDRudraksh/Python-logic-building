# 26. Write a Java program to find the largest and smallest element of an array.\


arr = [1,2,4,6,7,8,5,3]

# arr.sort()

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]


print(arr)           

print(arr[0],arr[-1])
