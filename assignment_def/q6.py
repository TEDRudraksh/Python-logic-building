# 6. Find the length of a string without using len().

def len_str():
    s = "dasjdashfjaffdasd"

    count=0
    for len in s:
        count+=1

    return count

result = len_str()
print(result)