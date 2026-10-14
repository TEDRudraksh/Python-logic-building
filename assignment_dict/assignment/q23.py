
# 23. Sort a dictionary by its values in ascending order.

dct = {'a': 10, 'b': 20,'d': 5, 'c': 7}
result = {}
while dct:
    low = float("inf")
    for key,value in dct.items():
        if value<low:
            low = value
            min = key
    result[min] = low
    dct.pop(min)
print(result)


