# 19. Count the frequency of every character using a dictionary.
# Example: "hello" → {'h': 1, 'e': 1, 'l': 2, 'o': 1}
def freq_count():
    s = "helloooo123"

    result = {}

    for i in s:
        if i in result:
            result[i]+=1
        else:
            result[i] = 1

    return result

result = freq_count()
print(result)