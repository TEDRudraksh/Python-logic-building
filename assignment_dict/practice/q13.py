# 13. Find the second-highest value in a dictionary without sorting it.


dic = {"a": 5, "b": 8, "c": 2}

highest = float('-inf')
second = float('-inf')
for key, value in dic.items():
    if value > highest:
        second = highest
        highest = value
    elif value > second:
        second = value

print(second)
