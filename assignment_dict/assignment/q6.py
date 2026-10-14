# 6. Remove a key from a dictionary using pop(). Handle the case where the
#    key does not exist.

student = {
    "name": "rudraksh",
    "age": 25,
    "marks" : {
        "maths": 50,
        "science": 70,
        "hindi": 60
    },
    "city": "indore"
}

target = "cit"

# if target in student:
#     popout = student.pop(target)
#     print(target,popout, "is pop out of dict")
# else:
#     print(target," does not exist")

# print(student)
result= student.pop(target,"not exist in dict")
print(result)
