# 35. Expand a compressed string.
# Example: "a3b2c4" → "aaabbcccc"

def compress():
    s = "a3b2c4"
    lst = []

    for i in range(len(s)):
        if s[i].isdigit():
            v = s[i-1]
            lst.append(v*int(s[i]))

    return print("".join(lst))

compress()
