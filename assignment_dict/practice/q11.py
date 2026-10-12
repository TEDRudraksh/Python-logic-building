# 11. Find common keys between two dictionaries and display their corresponding values.

dic1 = {"a":100,"b":11,"c":50}
dic2 = {"a":10,"b":1,"d":50}

result = {}
for key, value in dic1.items():
    if key in dic2:
        result[key] = [value, dic2[key]]

print(result)
