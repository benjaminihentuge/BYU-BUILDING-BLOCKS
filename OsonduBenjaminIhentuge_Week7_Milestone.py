print('WELCOME TO THE WORD GUESSING GAME')
print('---------------------------------')
print('\n')
play_again = 'yes'
while play_again == 'yes':
    secret_word = 'lucid'
    word_guess = 0
    guess_count = 1
    word_guess = str(input('what is your guess? '))

    while word_guess != secret_word:
        print('Your guess was not correct')
        word_guess = str(input('what is your guess? '))
        guess_count += 1
    print('congratulations You guessed it!')
    if guess_count == 1:
        print(f'it took you {guess_count} guess. LUCKY SHOT! ')
    else:
        print(f'it took you {guess_count} guesses ')

    play_again = str(input('''Do you want to play again?
Yes/no '''))

print('Thanks for playing. Hope you enjoyed the game')
k=input("Press enter to Exit")