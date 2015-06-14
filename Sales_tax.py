
purchase=float(input('Enter the amount of the item: '))
county_tax=.02*purchase
state_tax=.04*purchase
total_tax=county_tax+state_tax
total_cost=total_tax+purchase
print('An item that costs $', format(purchase,'.2f'),' has a county tax in the amount of $', \
format(county_tax,'.2f'),'and a state tax of $', format(state_tax,'.2f'),'for a total of $', format(total_tax,'.2f'),'in taxes.')
print('The total cost plus taxes is $', format(total_cost,'.2f'))

