# 10. Replace every space with a hyphen (-).

def replace_hyphen():
    s = "jsdnas dknsad nnaw nnd"
    lst = list(s)

    for i in range(len(lst)):
        if lst[i] == " ":
            lst[i] = "-"

    result = "".join(lst)
    return result

result = replace_hyphen()
print(result)
