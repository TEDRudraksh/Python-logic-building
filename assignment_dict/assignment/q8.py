
# 8. Calculate the sum of all numeric values in a dictionary.


student = {
    "name": "rudraksh",
    "age": 25,
    "marks" : 70,
    "city": "indore"
}
sum=0
for key,value in student.items():
    if isinstance(value,(int,float)):
        sum = sum + student[key]
print(sum)