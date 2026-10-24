# 31. Find the longest substring without repeating characters.
# Example: "abcabcbb" → 3 ("abc")

s = "abcdabcbb"
longest = ""

for i in range(len(s)):
    currnet = ""
    for j in range(len(s)):
        if s[j] in currnet:
            break
        currnet+=s[j]

    if len(currnet)>len(longest):
        longest = currnet

print(longest)
print(len(longest))





