# 11. Count how many times a particular character occurs.

s = "ndjasdhasbdhdbhsdasda"
lst = list(s)
result = {}

for i in range(len(lst)):
    if lst[i] in result:
        result[lst[i]]+=1
    else:
        result[lst[i]] = 1
print(result)


