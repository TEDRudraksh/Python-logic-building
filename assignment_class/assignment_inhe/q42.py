# 42. E-Commerce Order Processing

# Implement:

# products
# orders
# payment methods
# delivery system
products = []

class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        products.append({"name": self.__name, "price": self.__price})

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price


class Orders:
    def __init__(self, order_id):
        self.__order_id = order_id
        self.__orders = []

    def place_order(self):
        print("\nAvailable Products:")
        for i in products:
            print(i) 

        while True:
            choice = input("\nEnter product name to add (or 'done' to finish): ").strip()
            if choice.lower() == 'done':
                break

            found = False
            for item in products:
                if item["name"].lower() == choice.lower():
                    self.__orders.append(item)
                    print(f"Added {item['name']} to order.")
                    found = True
                    break
            
            if not found:
                print("Product not found. Try again.")

    def get_total(self):
        return sum(item["price"] for item in self.__orders)

    def get_order_details(self):
        return self.__order_id, self.__orders


class Payment(Orders):
    def __init__(self, order_id, payment_method):
        super().__init__(order_id)
        self.__payment_method = payment_method
        self.__is_paid = False

    def process_payment(self):
        total = self.get_total()
        if total == 0:
            print("Your order is empty. Nothing to pay.")
            return

        order_id, items = self.get_order_details()
        print(f"\n--- Receipt for Order #{order_id} ---")
        for item in items:
            print(f"- {item['name']}: ${item['price']}")
        print(f"Total Amount: ${total}")
        print(f"Payment Method: {self.__payment_method}")
        
        self.__is_paid = True
        print("Status: Payment Successful!")

    @property
    def is_paid(self):
            return self.__is_paid


class Delivery(Payment):
    def __init__(self, order_id, payment_method, address):
        super().__init__(order_id, payment_method)
        self.__address = address
        self.__status = "Pending"

    def dispatch_order(self):
        if not self.is_paid:
            print("Cannot dispatch order. Payment has not been completed.")
            return

        order_id, _ = self.get_order_details()
        self.__status = "Out for Delivery"
        print(f"\n--- Delivery Update for Order #{order_id} ---")
        print(f"Shipping Address: {self.__address}")
        print(f"Status: {self.__status}")
                


        
