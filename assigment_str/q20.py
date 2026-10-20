# 20. Remove duplicate characters while preserving their original order.
# Example: "programming" → "progamin"


s = "programming"
lst = list(s)
result = []
for i in range(len(lst)):
    if lst[i] in result:
        continue
    else:
        result.append(lst[i])

print("".join(result))