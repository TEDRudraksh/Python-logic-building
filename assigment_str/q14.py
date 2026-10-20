# 14. Remove all digits from a string.

s = "11223dadr44a22"

lst = []

for digit in s:
    ascii = ord(digit)
    if not(ascii>=48 and ascii<=57):
        lst.append(digit)

print("".join(lst))