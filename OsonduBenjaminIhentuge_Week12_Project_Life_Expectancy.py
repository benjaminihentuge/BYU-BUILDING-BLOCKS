import colorama
from colorama import (Style, Fore,)
colorama.init (autoreset= True)
max_exp = 0
min_exp = 100
year_submax_exp = 0
year_submin_exp = 1000
count_submax_exp = 0
count_submin_exp = 1000
year_average = 0
count_average = 0
year_total = 0  
count_total = 0 
sub_year_count = 0  
sub_count_count = 0    
choice_countryB = ''
#

print('\n')
print(Style.BRIGHT, Fore.CYAN +'LIFE EXPECTANCY PROGRAM'.center(150))
choice_year = input('Enter the year of interest? ')
# Added Creativity
# I introduced a loop to give the user an option of learning about the life expectancy of a country of their choice.

while True:
    choice_countryA = input('Do you wish to learn about the Life Expectancy of a certain country? ')
    if choice_countryA == 'yes':
        choice_countryB = input('Enter a country of interest ')
        break
    elif choice_countryA == 'no':
        break
    else:
        print('Please enter yes' or 'no')
print('')
with open('life-expectancy.csv') as file:
    for line in file: 
        line = line.strip()
        line = line.split(',')

        country_name = line[0]  
        code = line[1]
        year = line[2]
        life_exp = line[3]

        if life_exp != 'Life expectancy (years)':
            life_exp = float(life_exp)
        
            if life_exp > max_exp:
                max_exp = life_exp
                max_country = country_name
                max_year = year

            elif life_exp < min_exp:
                min_exp = life_exp
                min_country = country_name
                min_year = year

        if year == choice_year:
           
           choice_year = str(choice_year)
           life_exp = float(life_exp)
           year_submax_exp =float(year_submax_exp)
           sub_year_count += 1
           year_total += life_exp
           
           if life_exp > year_submax_exp:
                year_submax_exp = life_exp
                year_submax_year = year
                year_submax_country = country_name

           elif life_exp < year_submin_exp:
                year_submin_exp = life_exp
                year_submin_year = year
                year_submin_country = country_name

        elif country_name.lower() == choice_countryB.lower():


           choice_countryB = str(choice_countryB)
           country_name = str(country_name)
           life_exp = float(life_exp)
           count_submax_exp =float(count_submax_exp)
           sub_count_count += 1
           count_total += life_exp
           
           if life_exp > count_submax_exp:
                count_submax_exp = life_exp
                count_submax_year = year
                count_submax_country = country_name

           elif life_exp < count_submin_exp:
                count_submin_exp = life_exp
                count_submin_year = year
                count_submin_country = country_name

        

    if sub_year_count > 0:
        year_average = year_total / sub_year_count
    if sub_count_count > 0:
        count_average = count_total / sub_count_count
    print('')
    print('The overall max life expectancy is: {:.2f} from {:7} in {}'.format(max_exp,max_country,max_year))
    print('The overall min life expectancy is: {:.2f} from {:7} in {}'.format(min_exp,min_country,min_year))
    print('')
    print('For the year {}'.format(choice_year))
    
    print('The average life expectancy across all countries was {:.2f} '.format(year_average))
    print('The max life expectancy was {} with {:.2f} '.format(year_submax_country, year_submax_exp))
    print('The min life expectancy was {} with {:.2f} '.format(year_submin_country, year_submin_exp))
    print('')
   
    
    while choice_countryA == 'yes':
        print('For {}'.format(choice_countryB.capitalize()))
        print('The average life expectancy for {} {:.2f} '.format(choice_countryB.capitalize(), count_average))
        print('The max life expectancy for {} is {:.2f} '.format(choice_countryB.capitalize(), count_submax_exp))
        print('The min life expectancy for {} is {:.2f} '.format(choice_countryB.capitalize(), count_submin_exp))
        break
    print('')

