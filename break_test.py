# a = 0 % 3
# print(a)
# b = 1 % 3
# print(b)
# c = 2 % 3
# print(c)
# d = 3 % 3
# print(d)
# e = 4 % 3
# print(e)
# f = 5 % 3
# print(f)
# g = 6 % 3
# print(g)
# h = 7 % 3
# print(h)

# first_name ="In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."


# # Notice by using enumerate, we specify both i and letter
# for i, letter in enumerate(first_name):
#     print(f"The letter {letter} is at position {i}")




# word = 'commitment'

# fav_letter = str(input('what is your favorite letter? '))
# for letter in word:
#     if letter.lower() == fav_letter.lower():
#         print(letter.upper())
#     else:
#         print(letter.lower())





# word = 'commitment'
# fav_letter = str(input('what is your favorite letter? '))
# for letter in word:
#     if letter == fav_letter:
#         print( '_', end= '')
#     else:
#         print (letter.lower(), end= '')


# statement = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
# play_again = 'yes'
# while play_again == 'yes':
#     fav_num = int(input('what is your favorite number? '))

#     for i, letter in enumerate (statement):
#         if i % fav_num == 0:
#             print(letter.upper(), end='')
#         else:
#             print(letter.lower(),end='')
            
#     print()     
            
#     play_again = input('Do you wish to play again?')  
# print('Thank for playing')        

import random
import colorama
from colorama import Fore, Style, Back
colorama.init(autoreset= True)

print(Fore.GREEN + Style.BRIGHT + 'WELCOME TO THE WORD GUESSING GAME'.center(160))
print(Fore.GREEN + '---------------------------------'.center(160) )
print('\n')
print(f'{Fore.BLUE}<< {Fore.RED}I{Fore.RED}N{Fore.RED}S{Fore.RED}T{Fore.GREEN}R{Fore.GREEN}U{Fore.GREEN}C{Fore.CYAN}T{Fore.CYAN}I{Fore.CYAN}O{Fore.CYAN}N ' + '>>')
print(Fore.MAGENTA + Style.BRIGHT + '''You'll have to identify a prophet from the Book of Mormon by name in this game.
Each letter in the prophet's name will be a series of blanks that you must fill out. 
You will get a hint with the exact letters in the right positions and the wrong letters
in the appropriate spot for each guess. Check your knowledge of the prophet's name now!''')

#list of possible secret words
import random
secret_words = ['mosiah', 'nephi', 'ammon', 'helaman', 'alma', 'abinadi' ]

secret_word = random.choice(secret_words)
display = ['_' for letter in secret_word]

num_guesses = 0

while True:
    print(' '.join(display))
    guess = input(Style.DIM + Fore.BLUE + 'Guess a {}-letter word: '.format(len(secret_word)))
    num_guesses += 1

    if len(guess) != len(secret_word):
        print(Fore.RED + 'Your guess must have {} letters.'.format(len(secret_word)) + Style.RESET_ALL)
        continue

    if guess == secret_word:
        print(Fore.GREEN + 'Congratulations, you win!' + Style.RESET_ALL)
        print(Fore.YELLOW + 'Number of guesses: {}'.format(num_guesses) + Style.RESET_ALL)
        break

    hint = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint.append(secret_word[i].upper())
        elif guess[i] in secret_word:
            hint.append(guess[i].lower())
        else:
            hint.append("_")
    print(Fore.CYAN + 'Hint: {}'.format(' '.join(hint)) + Style.RESET_ALL)

play_again = str(input(Fore.GREEN + 'Do you want to play again? Yes/no ' + Style.RESET_ALL))
