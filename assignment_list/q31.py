# 31. Suppose X. Y, Z are arrays of integers of size M, N, and M + N respectively. The numbers in array X and Y appear in descending order. Write a java program to produce third array Z by merging arrays X and Y in descending order. 

arr1 = [5, 4, 3, 2, 1]
arr2 = [4, 2]
arr3 = []

i = 0
j = 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] > arr2[j]:
        arr3.append(arr1[i])
        i += 1
    else:
        arr3.append(arr2[j])
        j += 1

while i < len(arr1):
    arr3.append(arr1[i])
    i += 1

while j < len(arr2):
    arr3.append(arr2[j])
    j += 1

print(arr3)