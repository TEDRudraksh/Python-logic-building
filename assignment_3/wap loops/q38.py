n = int(input("Enter number: "))

original = n
temp = n
count = 0

while temp != 0:
    count = count + 1
    temp = temp // 10

temp = n
s = 0

while temp != 0:
    digit = temp % 10
    s = s + digit ** count
    temp = temp // 10

if s == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")