# 20. Reverse a dictionary so that values become keys and keys become values.
#     Assume all values are unique.

student = {
    "name": "rudraksh",
    "age": 25,
    "marks": 70
}

result = {}

for key,value in student.items():
    result[value] = key
print(result)