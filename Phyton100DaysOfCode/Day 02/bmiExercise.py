# This is a calculator of BMI with formula bmi = wheight (kg) / height2 (m2)
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# transform data tipe from str to float to make matematical operations
height_float = float(height)
weight_float = float(weight)
# formula
bmi = (weight_float/ (height_float*height_float))
#round bmi
bmi_round = round(bmi)
#printing our solution
print("Your bmi acording with your height ", height, " and your weight ", weight, " is: ", bmi_round)
