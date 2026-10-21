
# Q4. Sets — Common and Unique Elements (5 Marks)

# Given two lists, find:

# Elements common to both lists.

# Elements that appear in either list but not in both.

# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 60, 70]


list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60,70]

s_common = set()
s_eiter = set()

for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            s_common.add(list1[i])

for i in range(len(list1)):
    if list1[i] not in s_common:
        s_eiter.add(list1[i])

for i in range(len(list2)):
    if list2[i] not in s_common:
        s_eiter.add(list2[i])

print(s_common)
print(s_eiter)