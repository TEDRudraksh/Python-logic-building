# Q.8
# Given an unsorted array arr[] of size N having both negative and positive integers. The task is place all negative element at the end of array without changing the order of positive element and negative element.

# Example 1:
# Input : 
# N = 8
# arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
# Output : 
# 1  3  2  11  6  -1  -7  -5


arr = [1, -1, 3, 2, -7, -5, 11, 6 ]
postive = []
negative = []

for element in arr:
    if element>=0:
        postive.append(element)
    else:
        negative.append(element)

arr = postive + negative
print(arr)
