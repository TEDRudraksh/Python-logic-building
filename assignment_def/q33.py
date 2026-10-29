# 33. Check whether a string has balanced parentheses.[Stack]
# Example: "{[()]}" → True, "([)]" → False

def str_bal():
    s = "{[()]}"
    lst = []
    open = {"{","[","("}
    pairs = {"}": "{", "]": "[", ")": "("}
    for i in s:
        if i in open:
            lst.append(i)
        else:
            if not lst or lst[-1] != pairs[i]:
                return print(False)
                
            lst.pop()
    else:
       return print(len(lst) == 0)

str_bal()



