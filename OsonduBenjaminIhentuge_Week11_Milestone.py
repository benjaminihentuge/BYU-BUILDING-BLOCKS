#choice = input('Enter the year of interest? ')   
max_exp = 0
min_exp = 100

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

    print('The overall max life expectancy is: {:.2f} from {:7} in {}'.format(max_exp,max_country,max_year))
    print('The overall min life expectancy is: {:.2f} from {:7} in {}'.format(min_exp,min_country,min_year))
# submax_exp = 0
# submin_exp = 1000
# average = 0
# total = 0
# print('')
  
# print('')     
# with open('life-expectancy.csv') as file:
#     for line in file: 
#         line = line.strip()
#         line = line.split(',')

#         country_name = line[0]  
#         code = line[1]
#         year = line[2]
#         life_exp = line[3]

#         if year == choice:
#            choice = str(choice)
#            life_exp = float(life_exp)
#            submax_exp =float(submax_exp)
           
           
#            if life_exp > submax_exp:
#                 submax_exp = life_exp
#                 submax_year = year
#                 submax_country = country_name

#            elif life_exp < submin_exp:
#                 submin_exp = life_exp
#                 submin_year = year
#                 submin_country = country_name

#            elif life_exp == float(life_exp):
#                 total += submin_exp
#                 average = total/ (submax_exp)
   
        

    
            
#     print('For the year {}'.format(choice))
#     print(total)
#     print('The average life expectancy across all countries was {:.2f} '.format(average,))
#     print('The max life expectancy was {} with {:.2f} '.format(submax_country, submax_exp))
#     print('The min life expectancy was {} with {:.2f} '.format(submin_country, submin_exp))
                  

# print('\n')





