# # import random

# # number = random.randint(1, 10)

# # # number = int(input('What is the magic number?'))
# # guess = int(input('what is your guess?'))
# # while True:
# #     if guess == number:
# #         print('You guessed it!')
# #         break
        
# #     else:
# #         while guess > number:
# #             print ('Lower')
# #             guess = int(input('what is your guess?'))    
# #         while guess < number:
# #             print ('Higher')
# #             guess = int(input('what is your guess?'))   
            
      
       
import random
again = 'yes'
while again.lower() == 'yes':
    number = random.randint(1, 10)
    guess_number = 0
    guess_count = 0

    while guess_number != number:
            guess_number = int(input('what is your guess?'))      


            guess_count = guess_count + 1
            if guess_number > number:
                print('lower')
            elif guess_number < number:
                print('Higher')
    print('You guessed it!')
    print(f'it took you {guess_count} guesses.')
    
    again = input('would you like to play again? Yes/no ')
print('Thanks for Playing Hope you enjoyed it.')
