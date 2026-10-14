
# 11. Create a dictionary from two lists: one list contains keys and the
#     other contains values. Do not use zip().

lst1 = ["name","marks","city","location"]
lst2 = [1,2,3,4]

result = {}


for key in range(len(lst1)):
     result[lst1[key]] = lst2[key]

print(result)