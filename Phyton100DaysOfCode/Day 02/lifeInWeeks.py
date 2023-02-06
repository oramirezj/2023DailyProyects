# calculate your remanenting life in week, months, and days if you are going to live 90 years
#first ask your age
myAge = input("What's you currente age? ")
# so we have some important data 1 year = 12 months; 1 year = 52 weeks; 1 year = 365 days
# First we have to convert data from input from str to int
myAge_int = int(myAge)
#then we have to se how many years left you according with the premise
myLifeLeft = 90 - myAge_int
#then calculate days, weeks and months left of life
days = myLifeLeft * 365
weeks = myLifeLeft * 52
months = myLifeLeft * 12
#to see better how it looks on print we format the numbers to have , bettewn thousands
formated_days = "{:,}".format(days)
formated_weeks = "{:,}".format(weeks)


# Ok just need to print the result in days, months and years using f-string
print(f"You have {formated_days} days, {formated_weeks} weeks and {months} months left")