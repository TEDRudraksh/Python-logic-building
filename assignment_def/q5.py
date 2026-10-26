# 5. Count the number of words in a sentence.


def count_sentence():
    s = "words are not good for us"
    s = s.split()
    lst = list(s)

    count=0
    for i in range(len(lst)):
        count+=1
    return count

result = count_sentence()
print(result)