# 24. Write a Java program to swap first and last element of an integer 1-d array.

arr=[2,4,5,7,8]

last = arr[-1]
first = arr[0]

arr[0],arr[-1]=last,first
print(arr)