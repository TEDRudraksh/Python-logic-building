# 2. Given a dictionary of student details, print each key and value on a
#    separate line.


student = {
    "name": "rudraksh",
    "age": 25,
    "marks" : {
        "maths": 50,
        "science": 70,
        "hindi": 60
    }
}


for key,value in student.items():
    print(key, student[key])