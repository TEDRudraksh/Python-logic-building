# 25. Write a Java program to reverse the element of an integer 1-D array. 

arr = [2,4,5,3,4,6,5]
i=0
j=len(arr)-1
for _ in range(len(arr)):
    if i<j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j+=-1
print(arr)