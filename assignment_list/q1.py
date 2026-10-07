arr = [1,2,4,5,6,7]

if len(arr) == 0:
    print("0")
elif len(arr) == 1:
    print("1")
else:
    for i in range(1,len(arr)-1):
        if arr[i]>arr[i-1]and arr[i]<arr[i+1]:
            print("1")
            break
        else:
            if arr[-1]>arr[-2]:
                print("1")
                break
            else:
                print("0")
                break
    else:
        print("0")
        
