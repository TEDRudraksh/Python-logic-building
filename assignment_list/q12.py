arr1 = [1,2,4,5,6,7]
arr2 = [1,2,4,7]
arr3 = [1,2,3,5,6,7]
result = []

for element in arr1:
    if element in arr2 and element in arr3:
        result.append(element)
print(result)


#linear searach 