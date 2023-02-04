#ask fot a number of 2 digits then sume the number of the 2 digits. Ej. 23 = 2 + 3 = 5
number2Dig = input("Type a two digits number: ")
#the input format is str
#This proces is to separate the numbers 
firstDig = number2Dig[0]
secondDig = number2Dig[1]
#Then change the type from str to int so we can sume the numbers
num_firstDig = int(firstDig)
num_secondDig = int(secondDig)
#At the end just sum and print in the same line
print("The sum of the typed numbers is: ", num_firstDig+num_secondDig)
