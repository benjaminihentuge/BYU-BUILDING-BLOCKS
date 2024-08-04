import random

print('GUESSING GAME'.center(150))
print('-------------'.center(150))

secret_words = ['lucid', 'benjamin']
secret_word = random.choice(secret_words)

display = ['_' for letters in secret_word]

print(' '.join(display))
 
guess = input( 'input a {} letter word: ' .format(len(secret_word)))


if len(guess) != len(secret_word):
    print('please input a {} letter' .format(len(secret_word)))

if guess == secret_word:
    print ('CONGRATULATION YOU GOT IT!')

hint = []

for i in range(len(secret_word)):
    if guess [i] == secret_word [i]:
        hint.append(secret_word[i].upper())

    elif guess[i] in secret_word:
        hint.append(guess[i].lower())
    else:
        hint.append('_')
    
    print ('hint:{}'.format(''.join(hint)))
    
 




    