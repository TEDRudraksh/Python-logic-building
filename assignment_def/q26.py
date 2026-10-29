# 26. Find the longest word in a sentence.

def long_word():
    s = "this sentence contain longest word"

    s = s.split()
    high = 0
    for i in s:
        if len(i)>high:
            high = len(i)
            word = i

    return high,word

result = long_word()
print(result)