classes_held= int(input("enter classes held : "))
classes_attend= int(input("enter classes attend : "))
medical_reason= (input("medical reason yes/no? : ")).lower

percentage = (classes_attend/classes_held)*100

if medical_reason == "yes":
    print(f"you are eligible to attend exam")


if percentage>=75:
    print(f"classes attend : {percentage} %")
    print(f"you are eligible to attend exam")
else:
    print(f"classes attend : {percentage} %")
    print(f"you are not eligible to attend exam")

