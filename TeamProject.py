# lenght_of_the_square = float(input('what is the lenght of a side of  the square:'))
# area = lenght_of_the_square ** 2
# print(f'the area of the square is {area}')

# lenght_of_a_rectangle = float(input('what is the lenght of the rectangle:'))
# width_of_a_rectangle = float(input('what is the width of the rectangle:'))
# area_rectangle = lenght_of_a_rectangle * width_of_a_rectangle
# print(f'the area of the rectangle is {area_rectangle}')


# radius_of_circle = float(input('what is the radius of the circle:'))
# radius = 3.14  * (radius_of_circle ** 2)
# print(f'the radius of the circle is {radius} ')

# import math
# rad = float(input('what is the radius of the circle:'))
# radi = math.pi * (rad ** 2)
# print(f'the radius of the circle is {radi}')


# value =  float(input('input value that is to be used:'))

# area_of_the_square = value ** 2 
# radius_of_the_circle = math.pi * (value ** 2 )
# volume_of_the_cube = value ** 3
# volume_of_the_sphere = (4/3)  * math.pi * value **3 

# print(f'{area_of_the_square}')
# print(f'{radius_of_the_circle}')
# print(f'{volume_of_the_cube}')
# print(f'{volume_of_the_sphere}')
import math


def wind_chill_calculator(T, V):
    """
    Calculate the wind chill based on temperature and wind speed.

    Args:
        T (float): Temperature in Fahrenheit
        V (float): Wind speed in miles per hour

    Returns:
        float: Wind chill value
    """
    return 35.74 + 0.6215 * T - 35.75 * (V ** 0.16) + 0.4275 * T * (V ** 0.16)


def celsius_to_fahrenheit(C):
    """
    Convert a temperature in Celsius to Fahrenheit.

    Args:
        C (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    return C * 9 / 5 + 32


# Get temperature from user
temp = float(input('Enter the temperature: '))
unit = input('Is the temperature in Celsius or Fahrenheit? (C/F): ')

if unit.lower() == 'c':
    temp = celsius_to_fahrenheit(temp)

# Calculate wind chill for wind speeds from 5 to 60 mph
for wind_speed in range(5, 61, 5):
    wind_chill = wind_chill_calculator(temp, wind_speed)
    print(f"At wind speed {wind_speed} mph, the wind chill is {wind_chill:.2f}")







