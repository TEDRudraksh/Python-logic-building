# 12. Print all keys, all values, and all key-value pairs of a dictionary.


student = {
    "name": "rudraksh",
    "age": 25,
    "marks" : 70,
    "city": "indore"
}


for key,value in student.items():
    print("key",key,"value",value,"key : value" ,key , value)