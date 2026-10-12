# 4.
# Create a dictionary from two lists: one containing keys and the other containing values.


lst1 = [1, 2, 3, 4, 5, 6, 7]
lst2 = ["ok", "no", "value", "100", "yes", "y", "n"]

result = {}

for i in range(len(lst1)):
    result[lst1[i]] = lst2[i]

print(result)
