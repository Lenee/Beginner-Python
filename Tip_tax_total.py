#This program calculates tip, tax, total
Meal_cost=float(input("Please enter the amount of the meal: "))
tax=Meal_cost*.07
tip=Meal_cost*.15
total=Meal_cost+tax+tip
print('The tip amount is: $', format(tip,'.2f'),' and the tax amount is: $', format(tax,'.2f'),'!')
print("The total cost for the meal plus tip and tax is: $", format(total,'.2f'),'!')
