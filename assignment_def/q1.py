
def rev():
    s = "acdedfasf"

    rev = ""
    for i in s:
        rev = i + rev
    return rev

result = rev()
print(result)
