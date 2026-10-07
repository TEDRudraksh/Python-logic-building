# 30. Suppose A, B, C are arrays of integers of size M, N, and M + N respectively. The numbers in array A appear in ascending order while the numbers in array B appear in descending order. Write a java progtam to produce third array C by merging arrays A and B in ascending order. 

arr1=[2,3,4,6,7]
arr2=[7,6,3,2,1]
arr3=[]
arr2.sort()

s = min(len(arr1),len(arr2))

for i in range(s):
    if arr1[i]<arr2[i]:
        arr3.append(arr1[i])
        arr3.append(arr2[i])
    else:
        arr3.append(arr2[i])
        arr3.append(arr1[i])

for i in range(s,len(arr1)):
    arr3.append(arr1[i])

for i in range(s,len(arr2)):
    arr3.append(arr2[i])


print(arr3)