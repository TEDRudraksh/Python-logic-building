# 8. Remove all spaces from a string.

s = "anfifjaf fajsifj   jiajfiajf fff   "
lst = []

for ch in s:
    if ch == " ":
        continue
    else:
        lst.append(ch)

print(''.join(lst))
