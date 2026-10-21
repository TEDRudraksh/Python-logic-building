# Q3. Lists — Second-Largest Distinct Element (5 Marks)

# Given a list of integers, find the second-largest distinct element without using sort(), sorted(), or max().

# numbers = [12, 45, 7, 45, 30, 22, 30]

# Expected output: 30

numbers = [12,45,7,45,30,22,30]

high = float("-inf")
second = float("-inf")

for i in range(len(numbers)):
    if high<numbers[i]:
        second = high
        high = numbers[i]
    elif numbers[i]<high and numbers[i]>second:
        second = numbers[i]

print(second)
