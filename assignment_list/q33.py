arr = [1,2,4,5,6,7,8]

low = 0
high = len(arr)-1
target=6

while low<=high:
    mid = (low+high)//2

    if arr[mid]==target:
        print(f"element found : {mid}")
        break
    elif arr[mid]<target:
        low = mid+1
    else:
        high = mid-1

else:
    print("no element")