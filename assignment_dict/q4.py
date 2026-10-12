lst = ["apple","ant","bat","banana","cut","cherry"]
result = {}
for i in lst:
    key = i[0]
    if key in result:
            result[key].append(i)
    
    else:
            result[key] = [i]
            
print(result)