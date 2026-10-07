arr = [2, 3, 4, 5, 2]
k = 7

count = 0

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == k:
            count += 1

print(count)