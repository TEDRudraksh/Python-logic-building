# 23. Reverse the order of words in a sentence.
# Example: "Python is easy" → "easy is Python"
def rev_order():
    s = "Python is easy"
    s = s.split()
    lst = list(s)

    l = 0
    r = len(lst)-1
    for i in range(len(lst)):
        if l!=r:
            lst[l],lst[r] = lst[r],lst[l]
            l+=1
            r-=1
        else:
            break

    return print(" ".join(lst))

result = rev_order()
