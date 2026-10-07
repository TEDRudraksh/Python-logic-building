# 29. Suppose a one-dimensional array AR containing integers is arranged in ascending order. Write a java program to search for an integer from AR with the help of Binary search method, 


arr = [1,2,3,4,5,6,7,8]

low = 0
high = len(arr)-1
target=6

while low <= high:
    mid = low + (high - low) // 2

    if arr[mid] == target:
        print(f"Element found at index {mid}")
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")