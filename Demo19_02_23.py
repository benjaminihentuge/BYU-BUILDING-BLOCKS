# print('GUESSING GAME')
# print('-------------')
# print('-------------')

# Play_again = 'yes'
# while Play_again == 'yes':
  
#     guess_word = 'lucid'
#     guess_count = 1

#     guess = str(input('what is your guess?'))

#     while guess != guess_word:
#         guess_count = guess_count + 1
#         print('You Guessed It Wrong!')
#         guess = str(input('what is your guess?'))

#     print('congratulation you guessed it right!')
#     print(f'it took you {guess_count} guesses!')
#     Play_again = input('do yo want to play againg? yes/no')
    
# print('thanks for playing. hope you enjoyed the game!')



# items = ["crayon", "scissors", "paper", "glitter glue", "markers", "pens"]

# for item in items:
#     print(f"The item is: {item}")

# numbers = range(1000)

# for numbers in range(100, 200, 10):
#     print(numbers)

# for i in range(5):
#     print(i)
#     for j in range(10, 13):
#         print(f"--{j}")
#         for k in range(13, 15):
#             print(f'------{k}')



# first_name = "Brigham"

# fourth_letter = first_name[3] # Notice, using 3 instead of 4
# print(fourth_letter) # outputs a 'g' on the screen


# first_name = "Brigham"

# # Notice by using enumerate, we specify both i and letter
# for i, letter in enumerate(first_name):
#     print(f"The letter {letter} is at position {i}")




# colors = ["red", "blue", "green", "yellow"]
# for color in colors:
#     print(color)
# print('')
# print('')
# number = range(10)

# for number in range (1, 9):
#     print (number)
# print('')
# print('')
# number = range(21)

# for number in range (2, 21, 2):
#     print (number)

# word = ["commitment"]
# for letters in word:
#     print(word)
#     if letters == 'm':
#         print('')

# word = "commitment"

# favorite_letter = input("What is your favorite letter? ")

###
# Core Requirements #1 and #2
###
# for letter in word:
#     # Just in case the word or the user's letter contain a capital, we
#     # should convert the letters to lowercase when we compare them
#     if letter.lower() == favorite_letter.lower():
#         print(letter.upper(), end="")
#     else:
#         print(letter.lower(), end="")
# print()

# for letter in word:
#     # Just in case the word or the user's letter contain a capital, we
#     # should convert the letters to lowercase when we compare them
#     if letter.lower() == favorite_letter.lower():
#         print("_", end="")
#     else:
#         print(letter.lower(), end="")
# print()

# quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

# run_again = "yes"

# while run_again == "yes":
#     user_number = int(input("Please enter a number: "))

#     for i, letter in enumerate(quote):
#         # Remember that the % operator divides by a number and returns the remainder.
#         # So we can get every 3rd letter by dividing by 3 and looking for a remainder of 0,
#         # or more generically, we can divide by the user's number
#         if i % user_number == 0:
#             print(letter.upper(), end="")
#         else:
#             print(letter.lower(), end="")
    
#     # This puts a newline at the end of the list of quote
#     print()

#     run_again = input("Would you like to enter another number? ")

# print("Goodbye")

# function that adds two numbers
# def add_numbers(num1, num2):
#     sum = num1 + num2
#     return sum

# # calling function with two values
# result = add_numbers(5, 4)

# print('Sum: ', result)

# Output: Sum: 9 


# word = 'associaton'

# favorite_letter = str(input('what is your favorite letter '))

# for letter in word:
#     if letter.lower() == favorite_letter.lower():
#         print (letter.upper(), end='' )
#     else:
#         print(letter.lower(), end='')


# word = 'commitment'

# favorite_letter = str(input('what is your favorite letter? '))

# for letter in word:
#     if letter.lower() == favorite_letter.lower():
#         print ('_' , end='')
#     else:
#         print(letter.lower(), end='')


# word = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

# number = str(input('please input a number '))

# for i, letter in enumerate (word):
#     if 


# Program to capitalize every n-th letter in a given string
# Based on the quote: "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."


# secret = 'lucid'
# word_guess = ''
# guess_count = 1
# hint = 0

# print('your hint is _ _ _ _ _')
# word_guess = str(input('what is your guess? ').lower())

# for letter in secret:
#     if word_guess != secret:
#         print(f'your hint is {hint}')


#Additional creative element:
#Gave the user ability to title the story
#Capitalize the title using code
#Added 2 more adjectives to the story
#Added a sentence with "a" based on the starting letter of the adjective at the end.
print()
#prompt user to personally title the story
story_title= input('Title this Story:')
print()
#Example prompt insight
print('consider the following prompt before proceeding')
print()
print('adjective')
print('animal')
print('exclamation')
print('verb')
print()
#prompt the user for inputs
adjective= input('Enter an adjective:')
animal= input('Enter an animal:')
verb1= input('Enter a verb:')
exclamation= input('Enter an adjective:')
verb2= input('Enter another verb:')
adjective2= input('Enter another adjective:')
adjective3= input('Enter final adjective:')
print()
#show story title in upper case 
print(f'{story_title.upper()}')
print()
#Construct the story
print('The other day,i was really in trouble.It all started when i saw a very')
print("+adjective+''+animal+''+verb1+'down the hallway.")
print(f"{exclamation.capitalize()}'! i yelled.")
print('But all i could think to do was to'+verb2+'over and over. Miraculously,')
print('that caused it to stop,but not before it tried to'+verb2+"")
print('right in front of my family.')
print('A day like this would usually get me'+adjective2+'but i ended up feeling very'+adjective3+'.')
print()