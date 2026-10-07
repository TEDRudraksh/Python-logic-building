# 23. Write a Java program to find the sum and average of one dimensional integer array. 


arr = [1,3,4,5,2,6]
sum=0

for i in range(len(arr)):
    sum+=arr[i]
    avg = sum/(len(arr))
print(avg,sum)