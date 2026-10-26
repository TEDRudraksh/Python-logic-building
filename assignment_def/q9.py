# 9. Find the first and last character of a string.

def last_first():
    s = "ndnasdbjsjjdbnjsasdf"

    lst = list(s)

    result = lst[0],lst[-1]
    return result

result = last_first()
print(result)