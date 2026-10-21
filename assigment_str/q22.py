# 22. Find the second most frequent character.

s = "rruudraksh"

result = {}
for i in s:
    if i in result:
        result[i]+=1
    else:
        result[i] = 1

high = 0
second = 0
for key,value in result.items():
    if value>high:
        high = value
        ch = key
    elif value<high and second<value:
        second = value
        ch_second = key

print(result)
print(ch_second)