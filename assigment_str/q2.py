# 2. Check whether a string is a palindrome.

s = "6@12@21#**"
rev = ""
for i in s:
    if i.isalnum():
        rev = i + rev

pal = ""
for i in rev:
    pal = i + pal

if pal == rev:
    print("it is palindrome")
else:
    print("it is not palindrome")


