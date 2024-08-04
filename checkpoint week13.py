# # import datetime


# # def calabaasa():
# #     print('task complete')
# #     print(datetime.datetime.now())
# #     print()

   
# # first_name = 'susan'
# # calabaasa()
# # for x in range (0,10):
# #         print(x)
# # calabaasa()



# # first_name = input('Enter your first name: ')
# # first_name_initial = first_name[0:1]
# # last_name = input('Enter your last name: ')
# # last_name_initial = last_name[0:1]

# #print('your initials are: ' + first_name_initial + last_name_initial )

# # def get_initial(name):
# #       initial = name[0:1].upper()
# #       return initial

# # first_name = input('Enter your first name: ')
# # first_name_initial = get_initial(first_name)
# # last_name = input('Enter your last name: ')
# # last_name_initial = get_initial(last_name)

# # print('your initials are: ' + first_name_initial + last_name_initial )


# # def get_initial(name):
# #        initial = name[0:1].upper()
# #        return initial
# # first_name = input('Enter your first name: ')
# # last_name = input('Enter your last name: ')

# # print('your initials are: ' + get_initial(first_name) + get_initial(last_name) )


# # def print_double(value):
# #     double_value = value * 2
# #     print(double_value)

# # print_double(1902)

# # def get_double(value):
# #     double_value = value * 2
# #     return double_value
# # new_number = get_double(209)

# # print(new_number)



# # def print_statement_normal(state):
# #     normal = state
# #     return normal
# # def print_statement_upper(state):
# #     upper = state.upper()
# #     return upper
# # def print_statement_lower(state):
# #     lower = state.lower()
# #     return lower
# # statement = input('what is your statement? ')

# # print(print_statement_normal(statement))
# # print(print_statement_upper(statement))
# # print(print_statement_lower(statement))
# def display_numbers(x, y):
#     print(x)

# x = 3
# y = 4

# display_numbers(x, y)
# def display_numbers(x, y):

#     print(x)

# x = 3

# y = 4

# display_numbers(y, x)
# def display_numbers(x, y):

#     x = 10

# x = 3

# y = 4

# display_numbers(x, y)

# print(x)

# def display_numbers(x, y):

#     x = 10

# x = 3

# y = 4

# print(display_numbers(x, y))

# def display_numbers(x, y):
#     return 10

# x = 3
# y = 4
# x = display_numbers(x, y)

# print(x)

def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    

    # Complete the while loop condition.
    while number != 0:
        result = number * multiplier 
        if  result > 25 :
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        
        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3) 
# Should print: 
# 3x1=3 
# 3x2=6 
# 3x3=9 
# 3x4=12 
# 3x5=15

multiplication_table(5) 
# Should print: 
# 5x1=5
# 5x2=10
# 5x3=15
# 5x4=20
# 5x5=25

multiplication_table(8) 
# Should print:
# 8x1=8
# 8x2=16
# 8x3=24
