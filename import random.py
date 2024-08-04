# import random
# import colorama
# colorama.init(autoreset= True)
# from colorama import Style, Fore

# print(Fore.GREEN + Style.BRIGHT +'GUESS A COUNTRY'.center(150))
# secrets = ['nigeria', 'ghana', 'liberia', 'gambia', 'algeria', 'cameroon', 'mali', 'niger', 'chad', 'benin', 'egypt', 'gabon' 'guinea']
# secret = random.choice(secrets)
# guess_count = 0
# display = ['_' for letters in secret]
# import random

# print(' '.join(display))
# guess = input('Guess an African country with {} letters '.format(len(secret)))
# guess_count =+ 1
# if len(guess) != len(secret):
#     print('guess a country with {} letters'.format(len(secret)))

# if guess != secret:
#     print('your guess was not correct')

# if guess == secret:
#     print('CONGRATULATION YOU GUESSED IT RIGHT!')
#     if guess_count == 1:
#         print('IT TOOK YOU 1 GUESS')
#     else:
#         print('IT TOOK YOU {} GUEESES'.format(guess_count))


# hint = []

# for i in range(len(secret)):
#     if guess[i] == secret[i]:
#         hint.append((secret[i].upper()))
#     elif guess[i] in secret:
#         hint.append(guess[i].lower())
#     else:
#         hint.append('_')
# print(Fore.CYAN + 'Hint: {}'.format(' '.join(hint)) + Style.RESET_ALL)


print('Enter a list of numbers, type 0 when finished.')

# numbers = []
# number = ()
# total = 0

# while (number) != 0:
#     number = int(input('Enter number: '))
#     if number != 0:
#         numbers.append(number)
# for values in numbers:
#     total += values
# print('The sum is:{}'.format(total))































numbers = []
number = ()
total = 0
average = 0
max_number = 0


while (number) != 0:
    number = int(input('Enter number: '))
    if number != 0:
        numbers.append(number)

for values in numbers:

    total += values
    average =  total / (len(numbers))
    max_number = max(numbers)
print('The sum is:{}'.format(total))
print('The average is:{}'.format(average))
print('The largest number is:{}'.format(max_number))




