
# 27. Group words that are anagrams of one another.
#     Example: ["eat", "tea", "bat", "ate"]
#     Expected groups: ["eat", "tea", "ate"] and ["bat"]

lst = ["eat", "tea", "bat", "ate"]
result = {}


for i in range(len(lst)):
    val = "".join(sorted(lst[i]))
    if val in result:
        result[val].append(lst[i])
    else:
        result[val]=[lst[i]]
print(list(result.values()))