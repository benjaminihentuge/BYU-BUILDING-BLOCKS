# price = float(input('how much did you pay?'))
# if price >= 1.00:
#     tax = .07
#     print(f'tax rate is:' + str(tax)) 
# else:
#     tax = 0
#     print(f'tax rate is:' + str(tax))   

# country = 'canada'
# country = input('Please enter the name of your home country?')
# if country.lower() == 'canada':
#     print ('Oh look a Canadian')
# else:
#     print ('You are not from Canada')    

country = input('Please enter the name of your home country?')

if country.lower() == 'canada':
    town = input('what town do you reside in?')
    if town.lower() == 'jabi':
        tax =0.15
    elif town.lower() == 'utako':
        tax= 0.7
    elif town.lower() == 'lifecamp':
        tax = 0.13
    else:
        tax = 0.19
else: tax = 0
print (tax)