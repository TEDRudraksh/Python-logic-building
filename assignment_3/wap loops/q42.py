a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b:
    small = a
else:
    small = b

for i in range(1, small + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

print("HCF =", hcf)