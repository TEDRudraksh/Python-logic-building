# 2.
# Count the frequency of each character in a string.

s = "banana"

result = {}

for i in s:
    if i in result:
        result[i]+=1
    else:
        result[i] = 1

print(result)