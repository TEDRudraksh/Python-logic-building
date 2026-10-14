# 16. Count the frequency of each character in a string.
#     Example: "hello" -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}

student = "rudraksh"

result = {}

for c in student:
    if c in result:
        result[c]+=1
    else:
        result[c] = 1

print(result)

