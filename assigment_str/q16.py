# 16. Check whether two strings are anagrams.
# Example: "listen" and "silent" → True


s = "listen"
s1 = "silent"

for i in s:
    if i in s1:
        continue
    else:
        print("not anogram")
        break
else:
    print("True")