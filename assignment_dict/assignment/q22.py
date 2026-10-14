
# 22. Find the common keys between two dictionaries.


lst1 = {'a': 10, 'b': 20}
lst2 = {'b': 5, 'c': 7}


for key in lst1.keys():
    if key in lst2:
        print(key,end=' ')