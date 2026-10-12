# 7. Find the key with the highest frequency in a dictionary of word counts.

dic = {
    "name":4,
    "age":6,
    "status": 8,
    "earphone":5
}

high = 0
word = ""
for key,value in dic.items():
    if value>high:
        high = value
        word = key

print(word,high)
