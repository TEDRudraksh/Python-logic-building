physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))
biology = float(input("Enter Biology marks: "))
mathematics = float(input("Enter Mathematics marks: "))
computer = float(input("Enter Computer marks: "))

percentage = (physics + chemistry + biology + mathematics + computer) / 5

print(f"Percentage = {percentage}")

if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 40:
    print("Grade E")
else:
    print("Grade F")
