# get param
money_owed = float(input("How much money do you owe, in dollars?\n")) # 50,000
apr = float(input("What is the annual percentage rate?\n")) # 3.0
payment = float(input("What will your monthly payment be, in dollars?\n")) # 1,000
months = int(input("How many months do you want to see results for?\n")) # 24

monthly_rate = apr / 100 / 12

for i in range(months):
# 1st month
    interest = money_owed * monthly_rate
    money_owed = money_owed + interest - payment

    if money_owed < 0:
        print("THe last payment is ", payment + money_owed)
        print("You paid off the loan in ", i + 1, " months")
        break
    
    print("For month #", i + 1 ,": I have paid $", payment, " of which $", interest, " is interest. I now owe $", money_owed, ".", sep='')