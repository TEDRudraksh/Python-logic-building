customer_name = input("Enter your name : ")
customer_gender = input("Enter your Gender : ")

#for item 1
item1 = input("enter 1st item name : ")
item1_quantity = int(input("enter quantity"))
item1_price = 10
item1_totalprice = item1_quantity*item1_price

#for item 2
item2 = input("enter item name")
item2_quantity = int(input("enter the quantity"))
item2_price = 20
item2_totalprice = item2_quantity*item2_price

#for item 3
item3 = input("enter item name")
item3_quantity = int(input("enter the quantity"))
item3_price = 30
item3_totalprice = item3_quantity*item3_price

#for item 4
item4 = input("enter item name")
item4_quantity = int(input("enter the quantity"))
item4_price = 40
item4_totalprice = item4_quantity*item4_price

#for item 5
item5 = input("enter item name")
item5_quantity = int(input("enter the quantity"))
item5_price = 50
item5_totalprice = item5_quantity*item5_price

#for item 6
item6 = input("enter item name")
item6_quantity = int(input("enter the quantity"))
item6_price = 60
item6_totalprice = item6_quantity*item6_price

#for item 7
item7 = input("enter item name")
item7_quantity = int(input("enter the quantity"))
item7_price = 70
item7_totalprice = item7_quantity*item7_price

#for item 8
item8 = input("enter item name")
item8_quantity = int(input("enter the quantity"))
item8_price = 80
item8_totalprice = item8_quantity*item8_price

#for item 9
item9 = input("enter item name")
item9_quantity = int(input("enter the quantity"))
item9_price = 90
item9_totalprice = item9_quantity*item9_price

#for item 10
item10 = input("enter item name")
item10_quantity = int(input("enter the quantity"))
item10_price = 100
item10_totalprice = item10_quantity*item10_price


if item1_quantity>4:
    item1_discount_price = item1_totalprice - (item1_totalprice)*0.05
if item5:
    item5_discount_price = item5_totalprice - (item5_totalprice)*0.10
if item10:
    item10_discount_price = item10_totalprice - (item1_totalprice)*0.15

total_bill_afterdiscount =  item1_discount_price if item1_quantity>4 else item1_totalprice + item5_discount_price + item10_discount_price + item2_totalprice +item3_totalprice 
+ item4_totalprice + item6_totalprice + item7_totalprice + item8_totalprice + item9_totalprice

total_bill_beforediscount = item1_totalprice + item2_totalprice + item3_totalprice + item4_totalprice + item5_totalprice + item6_totalprice 
+ item7_totalprice + item8_totalprice + item9_totalprice + item10_totalprice

if total_bill_afterdiscount > 10000:
    total_bill_afterdiscount = total_bill_afterdiscount - (total_bill_afterdiscount)*0.15
if total_bill_afterdiscount >= 5000 and total_bill_afterdiscount<10000:
    total_bill_afterdiscount = total_bill_afterdiscount - (total_bill_afterdiscount)*0.10

total_bill_afterdiscount = total_bill_afterdiscount + (total_bill_afterdiscount)*0.10

total_gst = total_bill_afterdiscount + (total_bill_afterdiscount)*0.10




carry = input("do you want carry bag yes/no : ").lower
if carry == "yes":
    total_bill_afterdiscount = total_bill_afterdiscount + 10
    total_bill_Ap = total_bill_beforediscount + 10 + total_gst
    total_bill_dp = total_bill_beforediscount + 10 + total_gst
  
else:
    total_bill_afterdiscount = total_bill_afterdiscount
    total_bill_Ap = total_bill_beforediscount + total_gst
    total_bill_dp = total_bill_beforediscount + total_gst


if customer_gender == "female":
    gift = "cadebury"
else:
    gift = "leather wallet"


print("\t\t\tDmart")
print(f"Name : {customer_name}\tDate:15/09/26")
print("------------------------------------------------------")
print(f"{item1}\t\t{item1_quantity}\t\t{item1_price}\t{item1_totalprice}\t{item1_discount_price or item1_totalprice}")
print(f"{item2}\t\t{item2_quantity}\t\t{item2_price}\t{item2_totalprice}\t{item2_totalprice}")
print(f"{item3}\t\t{item3_quantity}\t\t{item3_price}\t{item3_totalprice}\t{item3_totalprice}")
print(f"{item4}\t\t{item4_quantity}\t\t{item4_price}\t{item4_totalprice}\t{item4_totalprice}")
print(f"{item5}\t\t{item5_quantity}\t\t{item5_price}\t{item5_totalprice}\t{item5_discount_price}")
print(f"{item6}\t\t{item6_quantity}\t\t{item6_price}\t{item6_totalprice}\t{item6_totalprice}")
print(f"{item7}\t\t{item7_quantity}\t\t{item7_price}\t{item7_totalprice}\t{item7_totalprice}")
print(f"{item8}\t\t{item8_quantity}\t\t{item8_price}\t{item8_totalprice}\t{item8_totalprice}")
print(f"{item9}\t\t{item9_quantity}\t\t{item9_price}\t{item9_totalprice}\t{item9_totalprice}")
print(f"{item10}\t\t{item10_quantity}\t\t{item10_price}\t{item10_totalprice}\t{item10_discount_price}")
print("------------------------------------------------------")
print("\t\t\tA.P\tD.P")
print(f"Gift : {gift}\t\t\t0.00\t0.00")
print("\n")
print(f"carry bag : {carry}\t\t\t{print("10.00\t10.00")if carry=="yes"else print("0.00\t0.00")}")
print(f"GST(10%)\t\t\t{total_gst}\t{total_gst}")
print("------------------------------------------------------")
print(f"\t\t\t\t{total_bill_Ap}\t{total_bill_dp}")
print("\n")
print("\t\t\tThank You")
print("\t\t\tto visit")
print("\t\t\tD-Mart")