# 7. Convert lowercase characters to uppercase without using upper().

s = "nnjdnjasbjbbA4321AANN"
lst = list(s)
for ch in range(len(lst)):
    ascii = ord(lst[ch])
    if ascii>=97 and ascii<=122:
        lst[ch] = chr(ascii-32)
        
print("".join(lst))