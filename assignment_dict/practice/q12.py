# 12. Sort a dictionary by its values in ascending order without using sorted().


# # dic1 = {"a": 10, "b": 1, "d": 50}
# result = {}
# while dic1:
#     lowest = None
#     lowest_key = None
#     for key, value in dic1.items():
#         if lowest is None or value < lowest:
#             lowest = value
#             lowest_key = key
#     result[lowest_key] = lowest
#     dic1.pop(lowest_key)
# print(result)









dic1 = {"a": 10, "b": 1, "d": 50}
result = {}
while dic1:
    lowest = 0
    low_key = None
    for key,values in dic1.items():
        if lowest == 0 or values<lowest:
            lowest = values
            low_key = key
    result[low_key] = lowest
    dic1.pop(low_key)
print(result)