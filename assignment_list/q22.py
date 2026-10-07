# Q.22) Java program to find nearest lesser and greater element in array
# Given an array of N elements and we have to find nearest lesser and nearest greater element using C program.
# Example:
#     Input:
#     Enter the number of elements for the arrray : 3  
 
#     Enter the elements for array_1.. 
#     array_1[0] : 1   
#     array_1[1] : 2   
#     array_1[2] : 3   
 
#     Enter the number : 2 
 
#     Output:
#     Element lesser than 2 is : 1 
#     Element greater than 2 is : 3

arr = [1, 3, 4, 5, 2, 6]
k = 6
arr.sort()
print(arr)
for i in range(len(arr)):
    if arr[i] == k:
        if i == 0:
            print(f"greater number is {arr[i+1]}")
        elif i == arr[-1]:
            print(f"lesser number is {arr[-2]}")
        else:
            print(f"lesser no is  {arr[i-1]}")
            print(f"greater no is {arr[i+1]}")
        break

else:
    print("Not in list")