# 6. Shopping Cart and Checkout
# Intermediate
# Concepts: Loops, conditions, functions, lists, dictionaries
# Requirements
#     • Store products and prices.
#     • Allow customers to add items and quantities.
#     • Calculate item-wise and total costs.
#     • Apply discounts based on purchase value.
#     • Generate a final bill.
# Bonus: Implement removing an item and checking product availability.


def item_wise(price,quantity):
    return price*quantity

def final_bill(dis_total):
    bill = dis_total*.05
    final_bill = dis_total + bill
    return final_bill

def discount(total):
    if total>22000:
        discount = total*.05
        dis_total = total - discount
        return dis_total
    else:
        return total


def shopping_cart():
    product_price = {"Laptop": 20000,"Earphone": 2000,"Speaker": 1000,"Charger": 500}
    total = 0
    item = {}
    while True:
        print("\t\t\t\t------Menu-------")
        op =  int(input("""
                            Enter 1 for Laptop : Rs20000\n
                            Enter 2 for Earphone : Rs2000\n
                            Enter 3 for Speaker: Rs1000\n
                            Enter 4 for Charger: Rs500\n
                            Enter 5 for confirm the order\n"""))


        if op == 1:
            quantity = int(input("How many quantity?"))
            total += item_wise(product_price["Laptop"],quantity)
            if "Laptop" in item:
                item["Laptop"] += item_wise(product_price["Laptop"],quantity)
            else:
                item["Laptop"] = item_wise(product_price["Laptop"],quantity)
                    
        elif op == 2:
            quantity = int(input("How many quantity?"))
            total += item_wise(product_price["Earphone"],quantity)
            if "Earphone" in item:
                item["Earphone"] += item_wise(product_price["Earphone"],quantity)
            else:
                item["Earphone"] = item_wise(product_price["Earphone"],quantity)
        elif op == 3:
            quantity = int(input("How many quantity?"))
            total += item_wise(product_price["Speaker"],quantity)
            if "Speaker" in item:
                item["Speaker"] += item_wise(product_price["Speaker"],quantity)
            else:
                item["Speaker"] = item_wise(product_price["Speaker"],quantity)
        elif op == 4:
            quantity = int(input("How many quantity?"))
            total += item_wise(product_price["Charger"],quantity)
            if "Charger" in item:
                item["Charger"] += item_wise(product_price["Charger"],quantity)
            else:
                item["Charger"] = item_wise(product_price["Charger"],quantity)
        elif op == 5:
            print("Thank You")
            break

    while True:
        choice = input("Do you want to remove any item from order?(yes/no)")
        if choice.lower() == "yes":
            for key,value in item.items():
                print(f"Item-wise Total {key}:{value}")
            rm = input("what You want to remove?type it").title()
            if rm in item:
                value = item.pop(rm)
                total-=value
            else:
                print("Invalid Item")

        elif choice.lower() == "no":
            dis_total = discount(total)
            final = final_bill(dis_total)


            for key,value in item.items():
                print(f"Item-wise Total {key}:{value}")

            print(f"Original Bill without Discount : {total}")
            print(f"Discounted bill without Tax : {dis_total}")
            print(f"Final Bill with tax and discount : {final}")
            break
        else:
            print("Invalid Response")


shopping_cart()

