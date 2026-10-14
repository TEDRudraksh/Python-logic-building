# 21. Combine two dictionaries by adding the values of common keys.
#     Example: {'a': 10, 'b': 20} and {'b': 5, 'c': 7}
#     Expected: {'a': 10, 'b': 25, 'c': 7}

lst1 = {'a': 10, 'b': 20}
lst2 = {'b': 5, 'c': 7}


for key,value in lst2.items():
    if key in lst1:
        lst1[key] = lst1[key]+value
    else:
        lst1[key] = value
print(lst1)

