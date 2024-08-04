print('Welcome to the Shopping Cart Program')
print('')
shopping_list = []
prices = []
while True:
    print('')
    print('Please select one of the following: ')
    print('')   
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit') 
    action = input('Please enter an action: ')
    print('')  
    
    if action == '1':
        item = input('What item would you like to add? ').capitalize()
        price = input('What is the price of {}? '.format(item))
        try:
            price = float(price)
        except ValueError:
            print('Invalid price. Please enter a valid number.')
            continue
        shopping_list.append(item)
        prices.append(price)
        print('\'{}\' has been added to the cart.'.format(item))
        print('\n')
        
    elif action == '2':
        print('The contents of the shopping cart are:')
        for i in range(len(shopping_list)):
            print('{} {} - ${:.2f}'.format(i+1, shopping_list[i], prices[i]))
            
    elif action == '3':
        index = input('Which item would you like to remove? ')
        try:
            index = int(index)
        except ValueError:
            print('Invalid index. Please enter a valid number.')
            continue
        if index < 1 or index > len(shopping_list):
            print('Invalid index. Please enter a valid index.')
            continue
        item = shopping_list.pop(index-1)
        price = prices.pop(index-1)
        print('\'{}\' has been removed from the cart.'.format(item))
        print('\n')
            
    elif action == '4':
        total = sum(prices)
        print('The total price of the items in the shopping cart is ${:.2f}'.format(total))
        
    elif action == '5':
        print('Thank you. Goodbye.')
        print('\n')
        break
        
    else:
        print('Invalid action. Please enter a valid option.')
