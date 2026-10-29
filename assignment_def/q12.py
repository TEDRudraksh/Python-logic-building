# 12. Check whether two strings are equal without using == for the complete strings.
def str_compare():
    s = "abba"
    d = "abba"

    if len(s)!=len(d):
        return print("not same")
    else:
        for i in range(len(s)):
            if ord(s[i]) - ord(d[i]):
                return print("not same")
        else:
            return print("same")

result = str_compare()
