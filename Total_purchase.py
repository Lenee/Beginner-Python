sales_tax=0.06
sale_1=float(input('Enter the cost of the first item: '))
sales_2=float(input('Enter the cost of the second item: '))
sale_3=float(input('Enter the cost of the third item: '))
total_cost=((sale_1+sales_2+sale_3)*sales_tax)+(sale_1+sales_2+sale_3)
print('The total cost including tax is $',format(total_cost,'.2f'),'!')
