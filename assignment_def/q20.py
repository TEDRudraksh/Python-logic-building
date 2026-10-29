# 20. Remove duplicate characters while preserving their original order.
# Example: "programming" → "progamin"

def rem_dup():
    s = "programming"
    lst = list(s)
    result = []
    for i in range(len(lst)):
        if lst[i] in result:
            continue
        else:
            result.append(lst[i])

    return print("".join(result))

rem_dup()