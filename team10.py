print('Enter the names and balance of bank accounts (type: quit when done)')

accounts = []
balance = []

input_acc = ''
input_bal = ''
total = 0 
max_num = 0


while input_acc != 'quit':
        input_acc = str(input('What is the name of this account? '))
        if input_acc != 'quit':
            input_bal = float(input('What is the balance? '))
            accounts.append(input_acc)
            balance.append(input_bal)


            if input_acc == 'quit' and input_bal == '':
                
            
                for info in range(len(accounts)): 
                    if info != 'quit':
                        break
                for dig in range(len(balance)):
                    if balance[dig] != -1:
                        break


                
        print('Account Information:')
        print( '{} - {}'.format(accounts[0],balance[0]))
        print( '{} - {}'.format(accounts[1],balance[1]))
        print( '{} - {}'.format(accounts[2],balance[2]))

        for values in balance:
            total += values
            average = total / (len(balance))
            max_num = max(balance)

        print('Total: {:.2f}'.format(total))
        print('Average: {:.2f}'.format(average))

        
    
                

        
                    
                
        
    

