import math

# def lenght_of_the_square(area_square_value):
#     area_square_value = int(area_square_value)
#     square_area = area_square_value ** 2
#     return square_area 


    



# sq_ar = input('Enter a value for square area ')



# def compute_area_rectangle(area_rectangle_value):
#     area_rectangle_value = int(area_rectangle_value)
#     rec_area = area_rectangle_value 
#     ret = rec_len * rec_wid
#     return ret

# rec_len = int(input('Enter a value for rectangle lenght '))
# rec_wid = int(input('Enter a value for rectangle widght '))





# print(lenght_of_the_square(sq_ar))
# print(compute_area_rectangle(rec_len))

    

def compute_area_square(value):
    lenght_of_the_square = value ** 2
    return lenght_of_the_square


def compute_area_rectangle(area_rectangle_value):
    area_rectangle_value = int(area_rectangle_value)
    rec_area = area_rectangle_value 
    ret = rec_len * rec_wid
    return ret

def compute_area_circle(figure):
    radius = math.pi * figure ** 2
    return radius




while True:
    choice = input('What shape do you want to calculate? ')
    if choice.lower()  == 'square':

        len_sqr = int(input('what is the lenght of a side of  the square: '))
        print(f'The area of the square is', compute_area_square(len_sqr))
        
    elif choice.lower()  == 'rectangle':

        rec_len = int(input('Enter a value for rectangle lenght '))
        rec_wid = int(input('Enter a value for rectangle widght '))
        print(f'The area of the rectangle is',  compute_area_rectangle(rec_len))
        

    elif choice.lower()  == 'circle':

        area_cic = float(input('Enter a radius for circle '))
        print(f'The area of the circle is',  compute_area_circle(area_cic))
