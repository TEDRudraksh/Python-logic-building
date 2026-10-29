# 18. Find the first repeating character.
# Example: "programming" → r


def repeat():
    s = "programming"

    result = {}

    for i in s:
        if i in result:
            result[i]+=1
        else:
            result[i] = 1

    for key,value in result.items():
        if value>=2:
            return key

result = repeat()
print(result)