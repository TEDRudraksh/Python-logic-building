# 8. Invert a dictionary. Swap keys and values.
# Example: {'a': 1, 'b': 2} → {1: 'a', 2: 'b'}

dic = {'a': 1, 'b': 2}
result = {}

for key,value in dic.items():
    result[value] = key 


print(result)