# 15. Find the ASCII/Unicode value of each character using ord().
lst = []
def ascii():
    s = "aavvcsrfetg"

    for i in s:
        lst.append((ord(i)))

    return lst

reuslt = ascii()
print(reuslt)