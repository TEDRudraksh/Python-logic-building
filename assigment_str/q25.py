# 25. Check whether a string contains only digits without using isdigit().

s = "11243"

for i in s:
    ascii = ord(i)
    if ascii>=48 and ascii<=57:
        continue
    else:
        print("it does not contain only digit")
        break
else:
    print("it contain only digit")