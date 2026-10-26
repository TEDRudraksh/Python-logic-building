# 7. Convert lowercase characters to uppercase without using upper().

def low_to_upr():
    s = "nnjdnjasbjbbA4321AANN"
    lst = list(s)
    for ch in range(len(lst)):
        ascii = ord(lst[ch])
        if ascii>=97 and ascii<=122:
            lst[ch] = chr(ascii-32)
            
    result = "".join(lst)
    return result

result = low_to_upr()
print(result)