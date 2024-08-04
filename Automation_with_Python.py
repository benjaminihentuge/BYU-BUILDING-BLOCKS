# for n in range(6,18+1,3):
#     print(n*2)

# for n in range(19):
#     if n % 2 == 0:
#         print(n)
# for n in range(18+1):
#     print(n**2)

# for n in range(10):
#     print(n+n)

# 6

def even_numbers(n):
    count = 0
    current_number = 0
    while n <= current_number:  # Complete the while loop condition
        if current_number % 2 == 0:
            9# Increment the appropriate variable
        count+= 1# Increment the appropriate variable
    return count
    
print(even_numbers(25))   # Should print 13
print(even_numbers(144))  # Should print 73
print(even_numbers(1000)) # Should print 501
print(even_numbers(0))    # Should print 1

