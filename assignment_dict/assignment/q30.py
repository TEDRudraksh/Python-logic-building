# 30. Safely retrieve a value from a deeply nested dictionary. If any key is
#     missing, return a default value such as "Unknown".



student = {
    "name": "Rahul",
    "details": {
        "academic": {
            "course": "B.Tech",
            "branch": "Computer Science",
            "marks": {
                "Python": 85,
                "Java": 78,
                "SQL": 90
            }
        },
        "address": {
            "city": "Indore",
            "state": "Madhya Pradesh"
        }
    }
}


student = student.get("details",{}).get("academic",{}).get("course","unknown")
print(student)