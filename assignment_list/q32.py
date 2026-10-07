# 32. Given two arrays of integers A and B of sizes M and N respectively. Write a Write a java program, which will produce a third array named C. such that the following sequence is followed. 
# All even numbers of A from left to right are copied into C from left to right. 
# All odd numbers of A from left to right are copied into C from right to left. 
# All even numbers of B from left to right are copied into C from left to right. 
# All old numbers of B from left to right are copied into C from right to left.
# e.g., A is {3, 2, 1, 7, 6, 3} and B is {9, 3, 5, 6, 2, 8, 10} the resultant array C is {2, 6, 6, 2, 8, 10, 5, 3, 9, 3, 7, 1, 3} 


arr = [3,2,1,7,6,3]
arr2 = [9,3,5,6,2,8,10]
c = arr + arr2
f=0
l=len(c)-1

for i in range(len(arr)):
    if arr[i]%2==0:
        c[f]=arr[i]
        f+=1
    else:
        c[l]=arr[i]
        l-=1


for i in range(len(arr2)):
    if arr2[i]%2==0:
        c[f]=arr2[i]
        f+=1
    else:
        c[l]=arr2[i]
        l-=1
print(c)
