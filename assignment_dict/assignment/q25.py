# 25. Given a nested dictionary of students and their subject marks, calculate
#     each student's total marks and find the topper.


students = {
    "Rahul": {
        "Python": 85,
        "Java": 78,
        "SQL": 90
    },
    "Priya": {
        "Python": 92,
        "Java": 88,
        "SQL": 95
    },
    "Aman": {
        "Python": 76,
        "Java": 82,
        "SQL": 80
    },
    "Sneha": {
        "Python": 89,
        "Java": 94,
        "SQL": 91
    },
    "Rohit": {
        "Python": 80,
        "Java": 75,
        "SQL": 85
    }
}


result = {}
for key,value in students.items():
    total = 0
    for k,v in value.items():
        total+=v
    result[key] = total

high = 0
for key,value in result.items():
    if value>high:
        high = value
        name = key

print(name,high)
        