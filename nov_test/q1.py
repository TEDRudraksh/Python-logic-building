# Q1. Longest Substring Without Repeating Characters

# Write a Python program to find the length of the longest substring that contains no repeating characters.

# Example:
# Input: abcabcbb
# Output: 3

# Explanation: "abc" is the longest substring.

s = "abcabcbb"
sett = set()
a = 0
b = 0
length = []
for a in range(len(s)):
    ch = s[a]
    if ch in sett:
        while s[a] in sett:
            sett.remove(s[b])
            b+=1
    sett.add(s[a])

    if(len(sett))>len(length):
        length.append(len(sett))
        

print(max(length))


