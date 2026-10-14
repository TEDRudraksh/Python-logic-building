# 7. Find the number of key-value pairs in a dictionary without using len().


student = {
    "name": "rudraksh",
    "age": 25,
    "marks" : 70,
    "city": "indore"
}
count = 0
for key in student.keys():
    count+=1
print(count)