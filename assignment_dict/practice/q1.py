# 1.
# Create a dictionary of 4 students and their marks. Print the student who scored the highest marks.

d = {
    "1st" : {
             "name":"rudraksh",
             "marks":80
            },

    "2nd" : {
            "name":"aman",
            "marks":60
            },

    "3rd":  {
            "name":"rohan",
            "marks":70
            },
    "4th":  {
            "name":"ram",
            "marks":90
            }, 

}

highest = 0
student = ""

for i in d:
    if d[i]["marks"] > highest:
        highest = d[i]["marks"]
        student = d[i]["name"]

print("Student:", student)
print("Highest marks:", highest)