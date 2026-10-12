d1 = {
    "a":10,
    "b":5
}

d2 = {
    "a":1,
    "b":1,
    "c":6
}

# for key,value in d2.items():
#     if key in d1:
#         d1[key] = d1[key]+value
#     else:
#         d1[key] = value

# print(d1)


for key,value in d2.items():
    d1[key] = d1.get(key,0)+value

print(d1)