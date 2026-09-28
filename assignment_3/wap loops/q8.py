first = 0
next = 1
n=7
for i in range(1,n+1):
    print(first)
    after = first + next
    first = next
    next = after