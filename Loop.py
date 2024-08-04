# number= 6
# while number < 10:
#     number = int(input('what is the number?'))
# print('Finished with the loop')
# Start with the number 1
number = 1

# Keep looping as long as the number is less than or equal to 5
# while number <= 10000:
    # Display the number
    # print(f"The number is: {number}")
    
    # Update the number to be one more than it was
#     number = number + 1 

# print("Finished with the loop")








positive_number = 0

positive_number = int(input('Please Type a Positive Number'))
while positive_number < 0:
    print('Sorry, that is a negative number. Please try again.')
    positive_number = int(input('Please Type a Positive Number'))
else:
    print (f'the number is {positive_number}')

# candy = ''

# candy = str(input('can I have a candy?'))

# while candy.lower() == 'no':
#     candy = str(input('can I have a candy?'))
# else:
#     print('Thank You')



answer = ""

while answer != "yes":
    # This could be written as: 'while answer == "no":'
    # The difference would be how it treats other words, besides yes and no
    answer = input("May I have a piece of candy? ")

print ("Thank you.")