s = "aaaabbbccd"
result = {}

for ch in s:
    if ch in result:
        result[ch]+=1
    else:
        result[ch]=1
print(result)