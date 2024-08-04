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