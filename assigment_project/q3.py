# 3. ATM Banking Simulator
# Beginner–Intermediate
# Concepts: Nested conditions, loops, functions
# Requirements
#     • Verify a PIN.
#     • Display balance, deposit, withdrawal, and exit options.
#     • Prevent withdrawals exceeding the available balance.
#     • Reject invalid amounts.
#     • Use separate functions for deposit, withdrawal, and balance enquiry.
# Bonus: Allow only three PIN attempts.



def deposit(increment,balance):
    balance+=increment
    return balance


def withdrawal(decrement,balance):
        balance-=decrement
        return balance

def enquiry(balance):
    return balance
    


def atm():
    total_balance = 0
    increment = 0
    decrement = 0
    count = 4
    pin = int(input("please set your pin (length of 4)"))
    if len(str(pin))!=4:
        return print("pin is not according to format/Invalid Pin")
    else:
        while count:
            print("------ATM-------")
            c_pin = int(input("Enter your PIN : "))
            if c_pin == pin:
                break
            elif count==1:
                return print("maxiumum attempt reached")   
            else:
                 print("pin is incorrect\n try again ")
                 count-=1
        while True:
                print("------Menu-------")
                op =  int(input("what you want to do?\nEnter 1 for Balance\nEnter 2 for Withdrawal\nEnter 3 for Deposit\nEnter 4 for Exit\n"))

                if op == 1:
                    total_balance = enquiry(total_balance)
                    print(f"your Balance : {total_balance}")
                elif op == 2 :
                    decrement = int(input("Enter value you want to withdrawal : "))
                    if decrement>total_balance:
                        print("exceeding the available balance")
                    else:
                        total_balance = withdrawal(decrement,total_balance)
                        print("Withdrawal Success")
                elif op==3:
                    increment = int(input("Enter value you want to deposit : "))
                    total_balance = deposit(increment,total_balance)
                    print("deposit Success")
                elif op == 4:
                    print("Thank you ")
                    break
                else: 
                     print("Invalid option")
                     

atm()

            





