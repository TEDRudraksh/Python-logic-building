# 19. Count the frequency of every character using a dictionary.
# Example: "hello" → {'h': 1, 'e': 1, 'l': 2, 'o': 1}

s = "helloooo123"

result = {}

for i in s:
    if i in result:
        result[i]+=1
    else:
        result[i] = 1

print(result)