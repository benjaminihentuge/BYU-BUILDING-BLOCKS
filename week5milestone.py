#Week 5 Requirement
print('You are on a flight to spend the holidays with your family in Lagos, everthing seems fine for the first twenty minutes of the flight')
print ('until you noticed that the left wing of the plane is one fire, knowing fully well there are only two things to be done,')
print('A: sit still and pray or B: take a parachute and jump out the plane. What do you do?')
while True:
    option1 = str(input('what will you do?'))
    if option1.capitalize() == 'A':
        print('You decided to stay seated and pray. ')
        print('The following minutes were blurry and the captain made an announcement over the PA system')
        print('instructing everyone to remain calm and fasten their seat belts')
        print('Just as you fastened your seat belt, you heard a loud thud from the rear of the plane and the oxygen masks deployed.')
        print('A: panic and freeze B: put on the oxygen mask C:help the little child that is sitting next to you with his mask')
        while True:
            option2 = str(input('what will you do?'))
            if option2.capitalize()== 'A':
                print('nice')
                break
            elif option2.capitalize() == 'B':
                print('ok')
                break
            elif option2.capitalize() == 'C':
                print('Good')
                break
            else: print('wrong choice please select an option') 
        break
    elif option1.capitalize() == 'B':
        print ('You took the parachute and jumped out of the plane, you already know your way around it from your numerous jumpimg lessons so it wasn\'t hard')
        print('you glide through the sky and landed on the beach of a remote island')
        break
    else: print ('wrong choice please select an option')  
   

 