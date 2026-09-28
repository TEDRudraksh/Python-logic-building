n = int(input("Enter number: "))

last = n % 10

temp = n

while temp >= 10:
    temp = temp // 10

first = temp

print("Sum =", first + last)