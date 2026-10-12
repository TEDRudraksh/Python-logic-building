# 10. Separate even and odd numbers into two dictionaries based on their values.
# Example: {'a': 10, 'b': 15, 'c': 20} → {'even': {'a': 10, 'c': 20}, 'odd': {'b': 15}}

dic = {'a': 10, 'b': 15, 'c': 20}

result = {"even":{},"odd":{}}

for key,values in dic.items():
    if values%2==0:
        result["even"][key] = values
    else:
        result["odd"][key] = values

print(result)



