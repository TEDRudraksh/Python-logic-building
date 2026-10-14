# 28. Create a new dictionary containing only entries whose values are greater
#     than or equal to a given threshold. Do not modify the dictionary while
#     iterating over it.

prices = {
    "laptop": 55000,
    "mouse": 500,
    "keyboard": 1500,
    "monitor": 12000,
    "headphones": 2500,
    "printer": 8000
}

threshold = 5000

result = {}

for key,value in prices.items():
    if value>=threshold:
        result[key] = value

print(result)