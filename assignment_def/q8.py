# 8. Remove all spaces from a string.

def remove_spc():
    s = "anfifjaf fajsifj   jiajfiajf fff   "
    lst = []

    for ch in s:
        if ch == " ":
            continue
        else:
            lst.append(ch)

    result = ''.join(lst)
    return result

result = remove_spc()
print(result)
