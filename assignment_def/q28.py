# 28. Check whether one string is a rotation of another.
# Example: "abcd" and "cdab" → True

def rotation():
    s1 = "python"
    s2 = "ythonp"

    if len(s1) == len(s2) and s2 in s1+s1:
        return True
    else:
        return False

result = rotation()
print(result)