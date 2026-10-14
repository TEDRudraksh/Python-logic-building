
# 24. Group a list of words according to their length.
#     Example: ["cat", "apple", "dog", "mango"]
#     Expected groups: 3 -> ["cat", "dog"], 5 -> ["apple", "mango"]


lst = ["cat", "apple", "dog", "mango"]

result = {}

for word in lst:
    if len(word) in result:
        result[len(word)].append(word)
    else:
        result[len(word)] = [word]
print(result)

