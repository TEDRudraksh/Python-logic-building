# Q5. Dictionaries — Word Frequency (5 Marks)

# Write a program to count the frequency of each word in a sentence using a dictionary. Treat uppercase and lowercase words as the same.

# sentence = "Python is easy and Python is powerful"

# Expected output:

# {
#     'python': 2,
#     'is': 2,
#     'easy': 1,
#     'and': 1,
#     'powerful': 1
# }

sentence = "Python is easy and Python is powerful"
sentence = sentence.split()

result = {}
for i in range(len(sentence)):
    if sentence[i] in result:
        result[sentence[i]]+=1
    else:
        result[sentence[i]] = 1

print(result)

