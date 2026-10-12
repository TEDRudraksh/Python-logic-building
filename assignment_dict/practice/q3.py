# 3.
# Count the frequency of each element in a list.

lst = [1,2,3,2,1,5,4,6]

result = {}

for i in range(len(lst)):
    if lst[i] in result:
        result[lst[i]]+=1
    else:
        result[lst[i]] = 1

print(result)
