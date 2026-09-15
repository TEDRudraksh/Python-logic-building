quantity= int(input("enter the quantity"))
one_unit = 100
total = quantity*one_unit

if total > 1000:
    total = total - (total*0.10)
print(f"total cost for {quantity} is : {total}")