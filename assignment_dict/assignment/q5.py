# 5. Update the value associated with the key "marks".

student = {
    "name": "rudraksh",
    "age": 25,
    "marks" : {
        "maths": 50,
        "science": 70,
        "hindi": 60
    }
}


student["marks"]["maths"] = 90

print(student)