import math
#week3 Requirement
childs_meal = float(input('what is the price of a child\'s meal?$'))
adults_meal = float(input('what is the price of an adult\'s meal?$'))
#Showing Creativity and Exceeding Requirements
childs_drink = float(input('what is the price of a child\'s drink?'))
adults_drink = float(input('what is the price of a adult\'s drink?'))
num_children = int(input('how many children are there?'))
num_adult = int(input('how many adults are there?'))
tax_rate = float(input('what is the sales tax rate?$'))

value1 = childs_meal * num_children
value2 = adults_meal * num_adult
value3 = value1 + value2
value4 = (value3 * tax_rate) / 100
value5 = value4 + value3
print('\n')
print(f'subtotal: ${value3:.2f}')
# Week 4 Requirement
print(f'sales tax: ${value4:.2f} ')
print(f'Total: ${value5:.2f}')
print('\n')
value6 = float(input('what is the payment amount?$'))
value7 = value6 - value5
print(f'change: ${value7:.2f}')
print()
k=input("Press enter to Exit")


