# 1. Write a program to reverse a string without using slicing ([::-1]).

s = "acdedfasf"
rev = ""
for i in s:
    rev = i + rev
print(rev)


