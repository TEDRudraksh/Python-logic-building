price= int(input("enter the percenatge  : "))


if price>100000:
    tax = price*0.15 
    print(f"tax is {tax}")
elif price>50000  and price<=100000:
    tax = price*0.10
    print(f"tax is {tax}")
elif price<=50000:
    tax = price*0.05
    print(f"tax is {tax}")
