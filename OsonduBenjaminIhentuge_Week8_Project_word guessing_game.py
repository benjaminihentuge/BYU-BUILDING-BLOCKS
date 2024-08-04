




# the import coloroma module is used to display text in different colors and styles. I introduced this for creativity.
import colorama
from colorama import Fore, Style
colorama.init(autoreset= True)

print(Fore.RED + Style.BRIGHT +'-------------'.center(150))
print(Fore.GREEN + Style.BRIGHT +'GUESSING GAME'.center(150))
print(Fore.RED + Style.BRIGHT +'-------------'.center(150))

print(Fore.GREEN + Style.BRIGHT + 'Welcome to the word guessing game!')
print('\n')
print(f'{Fore.BLUE}<< {Fore.RED}I{Fore.RED}N{Fore.RED}S{Fore.RED}T{Fore.GREEN}R{Fore.GREEN}U{Fore.GREEN}C{Fore.CYAN}T{Fore.CYAN}I{Fore.CYAN}O{Fore.CYAN}N ' + '>>')
print(Fore.MAGENTA + Style.BRIGHT + '''You'll have to identify a prophet from the Book of Mormon by name in this game.
Each letter in the prophet's name will be a series of blanks that you must fill out. 
''')
play_again = 'yes'
while play_again == 'yes':


 
    import random
       # I introduced a list to put the names of Book of Mormon Prophets. I called the import random module to chose random names from the list
    secret_words = [ 'mosiah', 'nephi', 'ammon', 'helaman', 'alma', 'abinadi', 'moroni' , 'benjamin' 'amaleki', 'enos','lehi', 'omni', 'jacob', 'amos']

    secret_word = random.choice(secret_words)
    display = ['_' for letter in secret_word]
    guess_count = 0

    while True:
        print(' '.join(display))
        guess = input(Style.DIM + Fore.BLUE + 'Guess a Book of Mormon Prophet with a {}-letter name: '.format(len(secret_word)))
        guess_count += 1

        if guess != secret_word:
            print(Fore.RED + 'Your guess was not correct.'+ Style.RESET_ALL)
            



        if len(guess) != len(secret_word):
            print(Fore.RED + 'Your guess must have {} letters.'.format(len(secret_word)) + Style.RESET_ALL)
            continue

        if guess == secret_word:
            print(Fore.GREEN + 'CONGRATULATIONS YOU GUESSED IT!' + Style.RESET_ALL)
            if guess_count == 1:
                print(Fore.YELLOW + 'It took you 1 guess. LUCKY SHOT!' + Style.RESET_ALL)
                break
            else:
                print(Fore.YELLOW + 'It took you {} guesses'.format(guess_count) + Style.RESET_ALL)
                break
        

        hint = []
        for i in range(len(secret_word)):
            if guess[i] == secret_word[i]:
                hint.append(secret_word[i].upper())
            elif guess[i] in secret_word:
                hint.append(guess[i].lower())
            else:
                hint.append('_')
        print(Fore.CYAN + 'Hint: {}'.format(' '.join(hint)) + Style.RESET_ALL)

    play_again = str(input(Fore.GREEN + 'Do you want to play again? Yes/no ' + Style.RESET_ALL))
print(Fore.GREEN + 'Thanks for playing. Hope you enjoyed the game')
k=input(Fore.GREEN +'Press enter to Exit')
