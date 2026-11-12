# 17. Electricity Bill System
# Problem

# Generate electricity bill.

# Requirements

# Consumer should contain:

# consumer id
# units consumed
# Functionalities
# Calculate bill
# Add surcharge using static method
# Display bill summary


class Electricity:
    def __init__(self,consumer_id,unit_consumed):
        self.__consumer_id = consumer_id
        self.__unit_consumed = unit_consumed
        self.__bill = 0

    @staticmethod
    def surcharge(bill):
        bill = bill + (bill*0.10)
        return bill

    def calculate(self):
        self.__bill = self.__unit_consumed*5
        self.__bill = Electricity.surcharge(self.__bill)
        print("Bill Calculated")

    def display(self):
        print("Bill Summary")
        print(f" 5 rupee/Unit , total_bill : R {self.__bill} , Id : {self.__consumer_id}")

bill1 = Electricity(1122,500)
bill1.display()
bill1.calculate()
bill1.display()