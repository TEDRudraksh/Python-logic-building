# Q.14. Find the first non-repeating elment in given array of integers
# Find the first non-repeating element in a given array arr of N integers.
# Note: Array consists of only positive and negative integers and not zero.
# Example 1:
# Input : arr[] = {-1, 2, -1, 3, 2}
# Output : 3
# Explanation:
# -1 and 2 are repeating whereas 3 is 
# the only number occuring once.
# Hence, the output is 3.



# arr = [-1,-1,2,-1,3,2]
# for i in range(len(arr)-1):
#     count=0
#     for j in range(len(arr)):
#         if arr[i]==arr[j]:
#             count+=1
#     if count == 1:
#         print(arr[i])
#         break

# arr = [2,3,1,4,1,5,6,7,8,2]

# arr = [1,1,2,1,3,2]
# s = set()
# result = None
# for i in range(len(arr)-1,-1,-1):
#     if arr[i] in s:
#         result = arr[i]

#     s.add(arr[i])

# print(result)


arr = [1,1,2,1,2,1,3,2]
for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    if count == 1:
        print(arr[i])
        break


arr = [-1,2,-1,3,3,3,4,2]

n=len(arr)

for i in range(n):
    repeat = False
    for j in range(n):
        if i!=j and arr[i]==arr[j]:
            repeat = True
            break
    if not repeat:
        print(arr[i])
        break