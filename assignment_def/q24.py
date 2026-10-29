# 24. Reverse every word without changing the word order.
# Example: "Python is easy" → "nohtyP si ysae"

def rev_word():
    s = "python is easy"


    s = s.split()
    lst = []

    for i in s:
        for ch in i[::-1]:
            lst.append(ch)
        lst.append(" ")


    return print("".join(lst))

result = rev_word()