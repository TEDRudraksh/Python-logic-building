# 30. Find the longest common prefix among a list of strings.
# Example: ["flower", "flow", "flight"] → "fl"


lst = ["floower", "floow", "flooight"]
prefix = ""

for i in range(len(lst[0])):
    ch = lst[0][i]
    count = 0

    for word in lst:
        if i < len(word) and word[i] == ch:
            count += 1

    if count == len(lst):
        prefix += ch
    else:
        break

print(prefix)