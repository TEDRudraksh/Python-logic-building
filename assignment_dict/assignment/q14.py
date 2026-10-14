
# 14. Copy a dictionary into another dictionary. Explain whether changing a
#     nested object in the copy can affect the original.


student = {
    "name": "rudraksh",
    "age": 25,
    "marks" : 70,
    "city": "indore",
    "hobbies": ["music","cricket"]
}

studentcopy = student.copy()

studentcopy["hobbies"].pop()

print(student)
print(studentcopy)