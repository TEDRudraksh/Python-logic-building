
# 18. Find the first non-repeating character in a string using a dictionary.



lst = "abcbabcebsg"

result = {}

for element in (lst):
    if element in result:
        result[element]+=1
    else:
        result[element] = 1
print(result)
for key,value in result.items():
    if value==1:
        print(key)
        break

