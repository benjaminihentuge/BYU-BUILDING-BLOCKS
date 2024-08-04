#Week 5 Requirement
print('------------------------------------------------ADVENTURE GAME---------------------------------------------------')
print('instuctions')
print('please type the word in CAPS as your selected option')
print('')
print('You are flying to Lagos to spend the holidays with your family. Everything seems normal for the first 20 minutes,')
print('but then you notice that the left wing of the plane is on fire. You have two options:')
print('remain seated and pray or take a parachute and jump out of the plane. do you SIT or JUMP')
while True:
    print('')
    option1 = str(input('what will you do?'))
    print('')
    if option1.lower() == 'sit':
        print('')
        print('You decided to stay seated and pray. ')
        print('The following minutes were blurry and the captain made an announcement over the PA system')
        print('instructing everyone to remain calm and fasten their seat belts')
        print('Just as you fastened your seat belt, you heard a loud thud from the rear of the plane and the oxygen masks deployed.')
        print('You have two options: panic and freeze, put on an oxygen mask')
        print('Do you PANIC or WEAR')
        print('')
        while True: 
            print('')
            option1a = str(input('what will you do?'))
            print('')
            if option1a.lower() == 'panic':
                print('You panicked and couldn\'t conserve your oxygen, leading to your death.')
                print('GAME OVER')
                print('')
                break
            elif option1a.lower() == 'wear':
                print('You put on your oxygen mask and tightly gripped the armrests as the plane plummeted down,')
                print('feeling like a terrible amusement park ride.The crash landing into the Atlantic Ocean jolted')
                print('you back to reality. Recalling the safety instructions provided by the flight attendant,')
                print('you quickly unstrapped your seat belt and inflated your life vest.The water was rapidly rising,')
                print('so you didn\'t have much time. Remembering that your family heirloom was in your carry-on luggage,')
                print('you were torn between retrieving it and quickly swimming out the back door of the plane. ')
                print('Do you risk staying behind to grab the heirloom or make a quick escape through the back door?')
                print('Do you GRAB or SWIM?? ')
                while True:
                    print('')
                    option1aa = str(input('what will you do?'))
                    print('')
                    if option1aa.lower() == 'grab':
                        print('You remained behind to retrieve your grandfather\'s pocket watch. Later, you made a split-')
                        print('second decision to escape through the front door of the plane. You quickly swam to the ')
                        print('door and managed to get out just before the plane sank. You floated for approximately one ')
                        print('hour before being rescued by the Nigerian coast guard.')
                        break
                    elif option1aa.lower() == 'swim':
                        print('You tried to escape from the back door of the plane, but it was blocked by luggage.')
                        print('You attempted to swim back to the front door, but unfortunately, ')
                        print('you couldn\'t reach it in time before the plane sank and you drowned.')
                        print('')
                        print('GAME OVER')
                        break
                    else: print('Wrong choice please select an option') 
                break
            else: print('Wrong choice please select an option')
            
        break
    elif option1.lower() == 'jump':
        print('you took a parachute and jumped out of the plane.')
        print('you had previous experience with parachuting from your multiple jumping lessons, so it wasn\'t difficult for you.')
        print('you glided through the sky and eventually landed on the beach of a remote island.')
        print('Upon landing on the island, you explored the nearby forest and discovered a chest containing three items:')
        print('a SATPHONE, GOURD labeled fresh water, and a CROSSBOW. pick one of these items')
        option1b = str(input('which will you pick?'))
        print('')
        if option1b.lower() == 'satphone':
                print('You utilized a satellite phone to contact the Nigerian Coast Guard, who subsequently arrived to offer assistance.')
                break
        elif option1b.lower() == 'gourd': 
                print('You consumed the contents of the gourd, only to discover that it was contaminated and as a result,')
                print('you passed away due to poisoning.')
                print('GAME OVER')
                print('')
                break
        elif option1b.lower() == 'crossbow':
                print('You obtained the crossbow and set out to search for food, water,')
                print('and shelter. You lived in the jungle for a period of two weeks until you were discovered by a rescue team')
                break
        else: print('Wrong choice please select an option') 
    else:print ('Wrong choice please select an option')  
    print('\n')
    print('')
k = input('press enter to exit')
