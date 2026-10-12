# 6. Merge two dictionaries. If the same key exists in both, add their values.

dic1 = {"a":100,"b":11,"c":50}
dic2 = {"a":100,"d":11,"d":50}

result = {}

for key,value in dic1.items():
    dic2[key] = dic2.get(key,0)+value

print(dic2)
