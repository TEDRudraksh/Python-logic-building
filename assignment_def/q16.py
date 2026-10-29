# 16. Check whether two strings are anagrams.
# Example: "listen" and "silent" → True

def anagram():
    s = "listen"
    s1 = "silent"

    for i in s:
        if i in s1:
            continue
        else:
            return print("not anogram")
    else:
        return print("True")

result = anagram()