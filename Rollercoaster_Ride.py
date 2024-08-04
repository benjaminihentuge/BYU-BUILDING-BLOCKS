# First_Rider_Age = float(input('what is the age of the first rider?'))
# First_Rider_Height = float(input('what is the height of the first rider?'))
# print('Is there a second rider? yes/no') 

# Second_Rider  = str(input(''))
# if Second_Rider.lower() =='yes':
#     Second_Rider_Age = float(input('what is the age of the first rider?'))
#     Second_Rider_Height = float(input('what is the height of the first rider?'))
#     if First_Rider_Height < 36 or Second_Rider_Height < 36:
#         Ride= False
#     else:
#         if First_Rider_Age >= 18 or Second_Rider_Age >= 18:
#             Ride = True
#         else:
#             Ride = False
# if Second_Rider.lower() == 'yes':
#     if First_Rider_Age < 18 and Second_Rider_Age < 18:
#         if First_Rider_Age >=12 and Second_Rider_Age >= 12:
#             if First_Rider_Height >=52 or Second_Rider_Height >=52:
#                 Ride = True
#             else: 
#                 Ride = False
#         else: 
#                 Ride = False
    

# else: 
#     if First_Rider_Height >=18 and First_Rider_Age >=62:
#         Ride = True
#     elif First_Rider_Age >= 12 or First_Rider_Age <=17:
#         golden_passport =str(input('''Do you have a golden passport?
#                            Yes/No
#         ''' ))
#         if golden_passport.lower() == 'yes':
#             Ride = True
#         else:
#             Ride = False
#     else:   
#         Ride = False
    
# if Ride:
#     print ('cool')
# else:
#     print ('uncool')
        





can_ride = False

age1 = int(input('what is the age of the first rider?'))
height1 = int(input('what is the height of the first rider?'))

if age1>= 12 and age1 < 18:
    golden1 = input('does this rider have a golden ticket?')


is_second_rider = input('is there a second rider?')

if is_second_rider.lower() == 'yes':
    age2 = int(input('what is the age of the second rider?'))
    height2 = int(input('what is the height of the second rider?'))

    if age2>= 12 and age2 < 18:
        golden2 = input('does this rider have a golden ticket?')

    if height1 < 36 or height2 < 36:
        can_ride = False
    else:

