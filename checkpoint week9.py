
# friends = []
# new_friend = ''

# while new_friend != 'end':
#     new_friend= input('Type the name of a friend ')
#     if new_friend != 'end':
#         friends.append(new_friend)
# print('Your friends are:')    
# for friend in friends:
#     print (friend)


    

# shopping_list = []
# item = ''
    
# while True:
#     item = (input('What item would you like to add? ')).capitalize()
#     shopping_list.append(item)
#     # item_price = float(input('what is the price of {} '.format(item)))
#     print('\'{}\'has been added to the cart.'.format(item))
#     print('\n')
#     for w in shopping_list:
#         print(w)


# print('Enter a list of numbers, type 0 when finished.')

# numbers = []
# number = ()                 
# total = 0
# average = 0 
# max_num = 0
# while (number) != 0:
#     number = int(input('Enter number:'))
#     if number != 0:
#         numbers.append(number)
# for values in numbers:
#     print(values)
# for figures in numbers:
#     total += figures 
#     average = total / (len(numbers))
#     max_num = max(numbers)
#     min_num = min(numbers)
# print('The sum is: {}'.format(total))
# print('The average is: {}'.format(average))
# print('The largest number is: {}'.format(max_num))
# smallest_so_far = 99999999999
# for number in numbers:
#     if number > 0 and number < smallest_so_far:
#         smallest_so_far = number
# print('The smallest positive number is: {}'.format(smallest_so_far))
# numbers.sort()
# print('The sorted list is:')
# for w in numbers:
#     print(w)








# introduction message #
# print('Welcome to the Shopping Cart Program!\n'

# 'Please select one of the following:\n'
# '1. Add item\n'
# '2. View cart\n'
# '3. Remove item\n'
# '4. Compute total\n'
# '5. Quit\n')
# # User chioce #

# Item = []
# New_item = ""
# User_select = ""
    
# while New_item != 'quit':
#     User_select = input('Please enter action: ')
#     if User_select == '1':
#         New_item = input("what Item would you like to add: ")
#         Item.append(New_item)
#         for items in Item:
#             print(f"{items} has been added to cart")





    # for value in numbers:
    #     number += number

    # print('The sum is:{}'.format(number))










# print('Welcome to the Shopping Cart Program')
# print('')
# shopping_list = []
# item = ''
# while True:
#     print('')
#     print('Please select one of the following: ')
#     print('')   
#     print('1. Add item')
#     print('2. View cart')
#     print('3. Remove item')
#     print('4. Compute total')
#     print('5. Quit') 
#     action = str(input('Please enter an action: '))
#     print('')  
    
    
#     if action == '1':
        
        
#         item = str(input('What item would you like to add? ')).capitalize()
#         shopping_list.append(item)
#         # item_price = float(input('what is the price of {} '.format(item)))
#         print('\'{}\' has been added to the cart.'.format(item))
#         print('\n')
        
       
        
      
        
#     elif action == '2':
#           print('The content of the shopping cart are:')
#           for w in shopping_list:
#             if action == '2':
#                 print(w)

                        

        
        
#     elif action == '5':
#         print('Thank You. Goodbye')
#         print('\n')
#         exit()

#     else:
#         print('Please enter a valid option')


      
    


        

print('Enter the names and balance of bank accounts (type: quit when done)')

accounts = []
balances = []

input_acc = ''
input_bal = ''
total = 0 
max_num = 0


while input_acc != 'quit':
        input_acc = str(input('What is the name of this account? '))
        if input_acc != 'quit':
            input_bal = float(input('What is the balance? '))
            accounts.append(input_acc)
            balances.append(input_bal)

print('\nAccount Information:')
        
for i in range(len(accounts)):
    
        
    input_acc = accounts[i]
    if input_acc != 'quit':
        
                     
        print( '{} {} - {}'.format(i+1,accounts[i],balances[i]))
                
            
for values in balances:
    total += values
    average = total / (len(balances))
    
print('Total: ${:.2f}'.format(total))
print('Average: ${:.2f}'.format(average))

highest_acc = None
highest_bal = 0

for i in range(len(accounts)):
        name = accounts[i]
        balance= balances[i]

        if balance > highest_bal:
            highest_bal = balance
            highest_acc = name
    

print('Highest Balance:{} - {:.2f}'.format(highest_acc,highest_bal))
''''''
while True:


    index = int(input('Which item would you like to change? '))
    r_item = input('What is the new item? ')
    for i in range(len(accounts)):
        

        accounts[index] = r_item

    for i in range(len(list)):
        item = accounts[i]
        if item != 'quit':
            print(f"{i}. {item}")
                