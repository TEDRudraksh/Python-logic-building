# 4. Restaurant Billing System
# Beginner–Intermediate
# Concepts: Loops, conditions, functions
# Requirements
#     • Display a menu with item prices.
#     • Let customers select items and quantities.
#     • Calculate the running bill.
#     • Apply discounts based on the bill amount.
#     • Calculate the final bill, including tax.
# Bonus: Add coupon codes and repeat-order functionality.


def calculate_bill(price,quantity):
    return price*quantity

def tax(bill):
    bill = (bill*.05) + bill
    return bill

def discount(total):
    if total>=500:
        discount = total*.05
        dis_bill = total - discount
        return dis_bill
    else:
        return total
    
def billing_system():

    total = 0

    items1_price = 100
    items2_price = 200
    items3_price = 300
    items4_price = 400
    items5_price = 500


    while True:
        print("\t\t\t\t------Menu-------")
        op =  int(input("""
                            Enter 1 for Pasta : Rs100\n
                            Enter 2 for Idli : Rs200\n
                            Enter 3 for Noodles: Rs300\n
                            Enter 4 for Burger: Rs400\n
                            Enter 5 for Dosa: Rs500\n
                            Enter 6 for confirm the order\n"""))

        if op == 1:
            quantity = int(input("How many quantity?"))
            total += calculate_bill(items1_price,quantity)
        elif op == 2:
            quantity = int(input("How many quantity?"))
            total += calculate_bill(items2_price,quantity)
        elif op == 3:
            quantity = int(input("How many quantity?"))
            total += calculate_bill(items3_price,quantity)
        elif op == 4:
            quantity = int(input("How many quantity?"))
            total += calculate_bill(items4_price,quantity)
        elif op == 5:
            quantity = int(input("How many quantity?"))
            total += calculate_bill(items5_price,quantity)
        elif op == 6:
            break

    dis_bill = discount(total)
    final_bill = tax(dis_bill)
    print(f"original bill without discount : {total}")
    print(f"discounted bill without tax : {dis_bill}")
    print(f"final bill with tax and discount : {final_bill}")


billing_system()