# 5.
# Find the key associated with a given value in a dictionary.


dic = {"a": 100, "b": 200, "c": 300}

target = 200

for key, value in dic.items():
    if value == target:
        print(key)
