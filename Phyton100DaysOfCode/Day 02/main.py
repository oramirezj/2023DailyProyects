# This a program to ask about the bill, how many people eat, the % of tip then split the bill
print("Welcome to the tip calculator! ")
bill = input("What was the total bill? $")
people = input("How many people to split the bill? ")
tipPercentage = input("What percentage tip would you like to give? 10, 12 or 15%? ")
#convert all values to float
billFloat = float(bill)
peopleInt = int(people)
tipPercentageFloat = float(tipPercentage)
#Calculate the amount of how much will pay each people
totalTips= (billFloat * tipPercentageFloat) / 100
totalBill = billFloat + totalTips
payForEach = totalBill / peopleInt
#Print the result
print("Each person should pay: $", round(payForEach, 2))
