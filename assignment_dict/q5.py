l = ["any", "one", "not", "okay", "five", "three"]

result = {len(element): [] for element in l}

#{3:[],4:[],5:[]}
for element in l:
    result[len(element)].append(element)

print(result)


empty = {}

for element in l:
    key = len(element)
    if key in empty:
        empty[key].append(element)
    else:
        empty[key] = [element]
print(empty)