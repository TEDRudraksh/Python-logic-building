# 33. Check whether a string has balanced parentheses.[Stack]
# Example: "{[()]}" → True, "([)]" → False


s = "{[()]}"
lst = []
open = {"{","[","("}
pairs = {"}": "{", "]": "[", ")": "("}
for i in s:
    if i in open:
        lst.append(i)
    else:
        if not lst or lst[-1] != pairs[i]:
            print(False)
            break
        lst.pop()
else:
    print(len(lst) == 0)





