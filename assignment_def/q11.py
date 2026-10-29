# 11. Count how many times a particular character occurs.
def count_chr():
    s = "ndjasdhasbdhdbhsdasda"
    lst = list(s)
    result = {}

    for i in range(len(lst)):
        if lst[i] in result:
            result[lst[i]]+=1
        else:
            result[lst[i]] = 1
    return result

result = count_chr()
print(result)


