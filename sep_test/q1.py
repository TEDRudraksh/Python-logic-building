# Q1. Electricity Bill Calculator — if-elif-else

# Write a Python program to calculate the electricity bill based on the number of units consumed.

# Use the following slab rates:

# Units	Rate
# First 100 units	₹5/unit
# Next 100 units	₹7/unit
# Next 200 units	₹10/unit
# Above 400 units	₹12/unit

units = int(input("Enter the unit"))

rate_100 = 5
next_100 = 7
next_200 = 10
above_400 = 12
first = 0
second = 0


first = units*rate_100
if units >=200:
    second = (units*next_100) - first