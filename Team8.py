

word = 'commitment'
fav_letter = str(input('please input your favorite letter '))

for letter in word:
    if letter == fav_letter:
        print(letter.upper())
    else:
        print(letter.lower())

