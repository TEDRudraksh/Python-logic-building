# 27. Find all duplicate characters and their frequencies.
 
s = "sknajsfafnajsdssfjbfe"

result = {}

for i in s:
    if i in result:
        result[i]+=1
    else:
        result[i] = 1

for key,value in result.items():
    if value>=2:
        print(key,value)