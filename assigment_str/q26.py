# 26. Find the longest word in a sentence.

s = "this sentence contain longest word"

s = s.split()
high = 0
for i in s:
    if len(i)>high:
        high = len(i)
        word = i

print(word,high)