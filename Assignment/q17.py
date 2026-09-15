basic = int(input("Enter basic salary: "))

if basic <= 10000:
    hra = basic * 20 / 100
    da = basic * 80 / 100
elif basic <= 20000:
    hra = basic * 25 / 100
    da = basic * 90 / 100
else:
    hra = basic * 30 / 100
    da = basic * 95 / 100

gross = basic + hra + da

print(f"Gross Salary is {gross}")
