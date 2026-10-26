def palindrome():
    s = "6@12@21#**"
    rev = ""
    for i in s:
        if i.isalnum():
            rev = i + rev

    pal = ""
    for i in rev:
        pal = i + pal

    if pal == rev:
        return True
    else:
        return False

result = palindrome()
print(result)