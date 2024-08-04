import math
grade = float(input('what is your grade percentage'))
sign = ''
last_digit = grade % 10
if grade >= 90:
    letter = 'A'   
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
elif grade < 60:
    letter = 'F'  
else:print('you scored an F')

if last_digit >= 7:
        sign = '+'
elif last_digit < 3:
        sign = '-'
else: 
    sign = '' 

print(f'your grade letter is {letter}{sign}')

if grade >= 70:
    print('congratulation you passed the class!')
else: print('nice efforts, please try again next year')


