# print('WELCOME TO THE WORD GUESSING GAME')
# print('---------------------------------')
# print('\n')
# # play_again = 'yes'
# # while play_again == 'yes':





# secret = 'lucid'
# secrets = secret.upper()
# word_guess = 0
# guess_count = 1
# hint = ' '
# for letter in range(0,len(secrets)):
#     hint == '_'

# word_guess = str(input('what is your guess? ').lower())

# hint = ''
# for letter in (0,len(word_guess)):
#     if len(word_guess) != len(secrets):
#         print('input a five letter word')
# for i, in range(len(word_guess)):
#     if secrets[i] != word_guess[i] and word_guess[i] in secrets:
#         hint 
   

    
        
 
    
    



















    # print('congratulations You guessed it!')
    # if guess_count == 1:
    #     print(f'it took you {guess_count} guess. LUCKY SHOT! ')
    # else:
    #     print(f'it took you {guess_count} guesses ')

   
   
   
   







   
   
#     play_again = str(input('''Do you want to play again?
# Yes/no '''))

# print('Thanks for playing. Hope you enjoyed the game')
# k=input("Press enter to Exit")


# The hint is a rendering of the letters in the guess according to the following guidelines:

# An underscore _ indicates that the letter was not present in the secret word.

# A lowercase letter indicates that the letter was present somewhere in the secret word, but not at that position.

# An uppercase letter indicates that the letter was present at that exact spot in the secret word. (In other words,
#  if the second letter in the guess is also the second letter in the secret word, then that letter is shown as a capital.)







# Define the list of possible secret words
secret_word = 'lucid'
secret_word = secret_word.upper()
display = ['_'for letter in secret_word]
num_guesses = 0

# Loop until the user guesses the word
while True:
    # Show the current state of the word to the user
    print(" ".join(display))

    # Ask the user for their guess
    guess = input("Guess a {}-letter word: ".format(len(secret_word)))

    # Increment the number of guesses
    num_guesses += 1

    # Check if the guess has the correct number of letters
    if len(guess) != len(secret_word):
        print("Your guess must have {} letters.".format(len(secret_word)))
        continue

    # Check if the guess is correct
    if guess == secret_word:
        print("Congratulations, you win!")
        print("Number of guesses: {}".format(num_guesses))
        break

    # Provide a hint for the next guess
    hint = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint.append(secret_word[i].upper())
        elif guess[i] in secret_word:
            hint.append(guess[i].lower())
        else:
            hint.append("_")
    print("Hint: {}".format(" ".join(hint)))
