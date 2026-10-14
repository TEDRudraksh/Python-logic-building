# 26. Find the second-largest distinct value in a dictionary.



data = {
    "a": 45,
    "b": 78,
    "c": 23,
    "d": 90,
    "e": 68,
    "f": 65
}

high = float("-inf")
second = float("-inf")
for key,value in data.items():
    if value>high:
        second = high
        high = value
    elif value<high and value>second:
        second = value

print(second)
