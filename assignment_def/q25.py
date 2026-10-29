# 25. Check whether a string contains only digits without using isdigit().

def digit():
    s = "11243"

    for i in s:
        ascii = ord(i)
        if ascii>=48 and ascii<=57:
            continue
        else:
            return print("it does not contain only digit")

    else:
        return print("it contain only digit")

result = digit()