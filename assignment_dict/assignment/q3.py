
# 3. Check whether the key "age" exists in a dictionary.

student = {
    "name": "rudraksh",
    "age": 25,
    "marks" : {
        "maths": 50,
        "science": 70,
        "hindi": 60
    }
}

target = "age"

if target in student:
    print(target ,"exists in dic")
else:
    print(target, "not exists in dic")