# 10. Replace every space with a hyphen (-).


s = "jsdnas dknsad nnaw nnd"
lst = list(s)

for i in range(len(lst)):
    if lst[i] == " ":
        lst[i] = "-"

print("".join(lst))
