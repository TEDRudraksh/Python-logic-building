# 29. Remove a particular character from a string without using replace().
 
target = "r"
s = "ranger"

lst = list(s)

lst.remove(target)

print("".join(lst))