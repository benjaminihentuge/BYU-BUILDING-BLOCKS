#week3 Requirement
childs_meal = float(input('What is the price of a child\'s meal?'))
adults_meal = float(input('What is the price of an adult\'s meal?'))
#Showing Creativity and Exceeding Requirements
childs_drink = float(input('What is the price of a child\'s drink?'))
adults_drink = float(input('What is the price of an adult\'s drink?'))
num_children = int(input('How many children are there?'))
num_adult = int(input('How many adults are there?'))
tax_rate = float(input('What is the sales tax rate?'))
print('\n')
value1 = (childs_meal + childs_drink) * num_children
value2 = (adults_meal + adults_drink) * num_adult
subtotal = value1 + value2
sales_tax = (subtotal * tax_rate) / 100
total = sales_tax + subtotal
print('')
print(f'Subtotal: ${subtotal:.2f}')
# Week 4 Requirement
print(f'Sales tax: ${sales_tax:.2f} ')
print(f'Total: ${total:.2f}')
print('\n')
#Showing Creativity and Exceeding Requirements
#it is customary in the United States to leave a tip equivalent to 15% of the total bill, before taxes.
tip = float(input('What percentage of tip will you like to give?'))
print('\n')
tip_amount = (tip * subtotal) / 100
New_total = total + tip_amount
print(f'Tip  ${tip_amount:.2f}')
print(f'Total ${New_total:.2f}')
payment_amount = float(input('What is the payment amount?'))
change = payment_amount - (tip_amount + total)
print(f'Change: ${change:.2f}')
print('\n')
#Showing Creativity and Exceeding Requirements
print('Thank you for choosing our restaurant. We hope you enjoyed your meal and had a great experience.')
print()
k=input("Press enter to Exit")
