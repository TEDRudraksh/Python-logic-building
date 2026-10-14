# 9. Find the key associated with the largest value in a dictionary.

student = {
    "name": "rudraksh",
    "age": 25,
    "marks" : 70,
    "city": "indore"
}

high=float("-inf")
for key,value in student.items():
    if isinstance(value,(int,float)):
        if value>high:
            high = value
            high_key = key
print(high_key)