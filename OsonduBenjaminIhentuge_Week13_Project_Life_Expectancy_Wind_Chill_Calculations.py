import math 
import colorama
from colorama import Style, Fore
colorama.init(autoreset= True)
print('\n')
print(Fore.BLUE + Style.NORMAL+'Wind Chill Calculator'.center(150))
# Defined Formula
def wind_chill_calculator(formula):
    formula = 35.74 + 0.6215*T - 35.75*( V ** 0.16) + 0.4275*T *( V ** 0.16)
    return formula
# Temperature Converter 
def temperature_converter(Celcius):
    return Celcius * (9/5) + 32

T = float(input(Fore.BLUE + Style.NORMAL+'What is the temperature? '))
while True:
    
    choice = input(Fore.BLUE + Style.NORMAL+'Fahrenheit or Celsius? (F/C) ')
    if choice.lower() == 'c':
        T = temperature_converter(T) 
        break
    elif choice.lower() == 'f':
        break
    else:
        print(Fore.RED + Style.NORMAL+'Invalid choice. Please select (F/C).')
    
V = 0
V = int(V)
count = 0
# Loop through wind speed from 5 to 60 miles per hour, added the count variable to keep increasing by 5 until it reaches 60mph
while True:
    count += 1
    V += 5
    wind_chill = wind_chill_calculator(V)
    print(Fore.GREEN + Style.BRIGHT+ f'At temperature {T}F, and wind speed {V} mph, the windchill is: {wind_chill:.2f}F')
    if count == 12:
        break 
print('\n')
    




        

















