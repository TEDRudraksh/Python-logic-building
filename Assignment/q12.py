number = int(input("Enter number: "))

reverse = number%10
number = number//10

reverse = reverse * 10 + number % 10
number = number// 10

reverse = reverse * 10 + number % 10
number = number// 10

reverse = reverse * 10 + number % 10

print(reverse)



