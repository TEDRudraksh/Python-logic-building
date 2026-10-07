# Q.18) Find largest sum contigeous sub array
# Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

# Example 1:
# Input:
# N = 5
# Arr[] = {1,2,3,-2,5}
# Output:
# 9
# Explanation:
# Max subarray sum is 9
# of elements (1, 2, 3, -2, 5) which 
# is a contiguous subarray.
# Example 2:
# Input:
# N = 4
# Arr[] = {-1,-2,-3,-4}
# Output:
# -1
# Explanation:
# Max subarray sum is -1 
# of element (-1)


arr = [-1, -2, -3, -4]
# arr = [1,2,3,-2,5]

sum = arr[0]
max_sum = arr[0]
for i in range(1,len(arr)):

    if sum + arr[i] > arr[i]:
        sum = sum + arr[i]
    else:
        sum = arr[i]

    if sum > max_sum:
        max_sum = sum

print(max_sum)





# sum = arr[0]
# max_sum = arr[0]

# for i in range(len(arr)):
#     if sum + arr[i] > arr[i]:
#         sum = sum + arr[i]
#     else:
#         sum = arr[i]
#     if sum>max_sum:
#         max_sum = sum
# print(sum)




# sum=arr[0]
# max=arr[0]

# for i in range(len(arr)):
#     if sum + arr[i]>arr[i]:
#         sum = sum+arr[i]
#     else:
#         sum = arr[i]
#     if sum>max:
#         max = sum
# print(sum)
