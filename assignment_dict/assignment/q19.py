
# 19. Find all duplicate elements in a list and their frequencies.

lst = [1,2,4,2,4,5,6,2,1,6,7,5]

result = {}


for element in lst:
    if element in result:
        result[element]+=1
    else:
        result[element] = 1

for key,value in result.items():
    if result[key] >=2:
        print(key,":",value, ",",end='')
   

