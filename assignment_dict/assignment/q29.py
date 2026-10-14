# 9. Given two dictionaries, return the keys whose values are equal in both.

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40,
    "e": 50
}

dict2 = {
    "a": 10,
    "b": 25,
    "c": 30,
    "d": 45,
    "f": 50
}
result = {}
for key,value in dict1.items():
    if key in dict2 and dict1[key] == dict2[key]:
        result[key] = value
print(result)