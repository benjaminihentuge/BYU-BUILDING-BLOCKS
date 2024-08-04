# gpa = float(input('what is your GPA?'))
# lowest_grade= float(input('what is your Lowest Score?'))

# if gpa >= 90 and lowest_grade >= 80:
#     honour_roll = True
# else: honour_roll = False

# if honour_roll:
#     print('congratulation you made the honour roll')
# else:
#     print('Try again next time') 








# RATE YOUR YOURSELF ON A SCALE OF ONE TO TEN

Loan_Size= float(input('How  large is the loan'))
Credit_History = float(input('How good is your credit history?'))
Income = float(input('How high is your Income?'))
Down_Payment = float(input('how large is your down payment?'))

if Loan_Size >= 5:
    if Credit_History >=7 and Income >= 7:
        Grant = True
    elif Credit_History >=7  or Income >= 7:   
        if Down_Payment >= 5:
            Grant = True
        else:
            Grant = False
    else:
            Grant = False
else:
    if Credit_History <=4:
        Grant = False
    else:
        if Income>= 7 or Down_Payment >= 7:
            Grant = True
        elif Income>= 4 and Down_Payment >= 4:
            Grant = True
        else:
            Grant = False

if Grant:
    print('You are Qualified for the Loan')
else:
    print('You do not meet the requirements for this loan')









