# books = ['book', 'loud']



# for i in range(len(books)):
#     book = books[i] + 1
#     print(f"{i}. {book}")

# list = []
# item = ''
# print('Please enter the items of the shopping list (type: quit to finish):')
# while True:
#     items = input('Item: ')
#     list.append(items)

    

#     if items == 'quit':
        
#         print('The shopping list is:')
#         for item in list:
#             if item != 'quit':
#                 print(item)
                
        
#         print('')
#         print('The shopping list with indexes is:')
#         for i in range(len(list)):
#             item = list[i]
#             if item != 'quit':
#                 print(f"{i}. {item}")
                


        

       

#         index = int(input('Which item would you like to change? '))
#         r_item = input('What is the new item? ')
#         for i in range(len(list)):
            

#             list[index] = r_item

#         for i in range(len(list)):
#             item = list[i]
#             if item != 'quit':
#                 print(f"{i}. {item}")
import colorama
from colorama import Style, Fore              

print(Fore.BLUE + Style.BRIGHT+ 'Welcome to the Shopping Cart Program'.center(150))
print('')
shopping_list = []
prices = []
item = ''
item_price = ()
while True:
    print('')
    print(Fore.BLUE + Style.BRIGHT+ 'Please select one of the following: ')
    print('')   
    print(Fore.CYAN + Style.NORMAL+ '1. Add item')
    print(Fore.CYAN + Style.NORMAL+ '2. View cart')
    print(Fore.CYAN + Style.NORMAL+ '3. Remove item')
    print(Fore.CYAN + Style.NORMAL+ '4. Compute total')
    print(Fore.CYAN + Style.NORMAL+ '5. Quit') 
    action = str(input('Please enter an action: '))
    print('')  
    
    
    if action == '1': 
        item = str(input(Fore.GREEN + Style.DIM+'What item would you like to add? ')).capitalize()
        shopping_list.append(item)
        item_price = float(input('what is the price of {} '.format(item)))
        prices.append(item_price)
        print('\'{}\' has been added to the cart.'.format(item))
        print('\n')

    elif action == '2':
          print('The content of the shopping cart are:')

          for i in range(len(shopping_list)):
            if action == '2':
                # Added Creativity:  I added spacing so the prices will be aligned
                print( Fore.YELLOW + Style.NORMAL+'{}. {:15} ${:.2f}'.format(i+1,shopping_list[i],prices[i]))

    elif action == '3':           
        index = int(input(Fore.GREEN + Style.NORMAL+'Which item would you like to remove? '))

        if index < 1 or index > len(shopping_list):
            print(Fore.RED + Style.DIM+'Invalid index. Please enter a valid index.')
            continue
        item = shopping_list.pop(index-1)
        price = prices.pop(index-1)
        print(Fore.YELLOW + Style.NORMAL+'Item removed.')

    elif action == '4':
        total = sum(prices)

        print(Fore.YELLOW + Style.DIM+'The total price of the items in the shopping cart is ${:.2f}'.format(total))
                  
    elif action == '5':
        print(Fore.YELLOW + Style.NORMAL+'Thank You. Goodbye')
        print('\n')
        exit()

    else:
        print(Fore.RED + Style.DIM+'Invalid action. Please enter a valid option.')


      
    


        

