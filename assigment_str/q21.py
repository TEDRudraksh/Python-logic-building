# 21. Find the most frequent character in a string.

s = "rudraksh"

result = {}
for i in s:
    if i in result:
        result[i]+=1
    else:
        result[i] = 1

high = 0
for key,value in result.items():
    if value>high:
        high = value
        ch = key


print(result)
print(ch)