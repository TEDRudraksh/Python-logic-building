# 17. Find the first non-repeating character in a string.
# Example: "aabbcddee" → c


s = "abcaedfg"
dict1 = {}
for i in s:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i] = 1

for key,value in dict1.items():
    if value==1:
        print(key)
        break