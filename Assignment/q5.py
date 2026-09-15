age1= int(input("enter age  : "))
age2= int(input("enter age : "))
age3= int(input("enter age : "))

if age1>age2 and age1>age3:
    if age2>age3:
        print(f"oldest is {age1} and youngest is {age3}")
    else:
        print(f"oldest is {age1} and youngest is {age2}")
elif age2>age1 and age2>age3:
    if age1>age3:
        print(f"oldest is {age2} and youngest is {age3}")
    else:
        print(f"oldest is {age2} and youngest is {age1}")

elif age3>age1 and age3>age2:
    if age1>age2:
        print(f"oldest is {age3} and youngest is {age2}")
    else:
        print(f"oldest is {age3} and youngest is {age1}")