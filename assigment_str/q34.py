# 34. Compress a string by counting consecutive repeated characters.
# Example: "aaabbccccd" → "a3b2c4d1"


s = "aaabbcccc"
result = ""
count = 1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count+=1
    else:
        result+=s[i-1]+str(count)
        count = 1

result+=s[-1]+str(count)
print(result)