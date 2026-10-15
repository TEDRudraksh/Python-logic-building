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

result = set()

for key1, value1 in dict1.items():
    for key2, value2 in dict2.items():
        if value1 == value2:
            result.add(key1)
            result.add(key2)

print(result)