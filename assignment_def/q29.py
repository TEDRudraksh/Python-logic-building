# 29. Remove a particular character from a string without using replace().
 

def par_chr():
    target = "r"
    s = "ranger"

    lst = list(s)

    lst.remove(target)

    return print("".join(lst))

result = par_chr()