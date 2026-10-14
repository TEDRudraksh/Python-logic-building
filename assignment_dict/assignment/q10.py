# 10. Merge two dictionaries. If a key exists in both dictionaries, use the
#     value from the second dictionary.


student0 = {
    "name": "rudraksh",
    "age": 25,
    "marks" : 70,
    "city": "indore"
}

student1 = {
    "name": "hariom",
    "age": 24,
    "marks" : 90,
}


result = {}

for key,value in student0.items():
    if key in student1:
        result[key] = student1[key]
print(result)