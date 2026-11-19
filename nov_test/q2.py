

# Q2. String Anagram

# Write a program to check whether two given strings are anagrams of each other.

# Anagrams contain the same characters with the same frequency, but in a different order.
# Input:
# String 1: listen
# String 2: silent

# Output: Anagram

s1 = "listen"
s2 = "silent"

d1 = {}
d2 = {}

for i in s1:
    if i in d1:
        d1[i]+=1

    else:
        d1[i] = 1

for j in s2:
    if j in d2:
        d2[j]+=1
    else:
        d2[j] = 1

if d1==d2:
    print(True)
else:
    print(False)

