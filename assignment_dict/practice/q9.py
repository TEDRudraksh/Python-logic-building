# 9. Remove duplicate values from a dictionary while keeping the first occurrence.
# Example: {'a': 10, 'b': 20, 'c': 10} → {'a': 10, 'b': 20}

dic = {'a': 10, 'b': 20, 'c': 10}

result = {}

for key,value in dic.items():
    if key not in result and value not in result.values():
        result[key] = value

print(result)