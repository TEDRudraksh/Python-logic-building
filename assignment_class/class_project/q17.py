    # 7. Write a  program to create a class called "Bank" with a collection of accounts and methods 
    # to add and remove accounts, and to deposit and withdraw money. 
    # Also define a class called "Account" to maintain account details of a particular customer.

class Bank:
    def __init__(self):
        self.__accounts = []

    def add_account(self, account):
        self.__accounts.append(account)
        print("Account added successfully!")

    def remove_account(self, account):
        if account in self.__accounts:
            self.__accounts.remove(account)
            print("Account removed successfully!")
        else:
            print("Account not found!")

    def deposit(self, person):
        amount = int(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Invalid amount!")
            return

        person.set_balance(person.get_balance() + amount)
        print("Deposit successful!")

    def withdraw(self, person):
        amount = int(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount!")
        elif amount > person.get_balance():
            print("Insufficient balance!")
        else:
            person.set_balance(person.get_balance() - amount)
            print("Withdrawal successful!")


class Account:
    def __init__(self, name, age, accountno, balance):
        self.__name = name
        self.__age = age
        self.__accountno = accountno
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount

    def display(self):
        print("\nAccount Details")
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Account No: {self.__accountno}")
        print(f"Balance: {self.__balance}")




ban = Bank()
person1 = Account("Rahul", 25, 112233, 4500)
ban.add_account(person1)
person1.display()
ban.deposit(person1)
ban.withdraw(person1)
person1.display()
