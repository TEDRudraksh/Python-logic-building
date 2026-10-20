# 12. Check whether two strings are equal without using == for the complete strings.

s = "abba"
d = "abba"

if len(s)!=len(d):
    print("not same")
else:
    for i in range(len(s)):
        if ord(s[i]) - ord(d[i]):
            break
    else:
        print("same")