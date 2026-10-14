
# 17. Count the frequency of each number in a list.
#     Example: [1, 2, 2, 3, 1, 2] -> {1: 2, 2: 3, 3: 1}

lst = [1,2,4,2,4,5,6,3,1]

result = {}

for element in range(len(lst)):
    if element in result:
        result[element]+=1
    else:
        result[element] = 1

print(result)