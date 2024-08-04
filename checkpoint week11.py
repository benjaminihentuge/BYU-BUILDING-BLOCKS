# with open('books.txt') as file:
#     for line in file:
#         #line = line.strip()
#         parts= line.split(',')
        
#         #print(line)
       
        
#         books = parts[0]
#         num = float(parts[1])


#         add = num + 3
        
#         print(f'book:{books}  num  {num}       sum  {add}')




# colors = ('green ,yellow ,red ,white')

# words = colors.split(',')


# print(words)
# print(colors)


# name = '    Osondu         \n'

# clean_name = name.strip()
# print('-------------{}-----------------'.format(name))
# print('-------------{}-----------------'.format(clean_name))

# name = name.strip()
# print('-------------{}-----------------'.format(name))




# with open('books.txt') as file:
#     for line in file: 
#         line = line.strip()
#         print(line)
# line = "     text"

# line.strip()

# print(line)     

print('\n')

choice = input('What volume of scripture would you love to learn about? ' )

print('')
largest_chapter = 0
largest_book =''


with open('books_and_chapters.txt') as standard_works:
    for books in standard_works:
        books = books.strip()
        books = books.split(':')

        book = books[0]
        chapters = int(books[1])
        scripture = books[2]


  
        if scripture == choice:
            if chapters > largest_chapter:

                largest_chapter = chapters
                largest_book = book
                


    print('The book with the largest number of chapters in the {} is {} with {} chapters.'.format(choice, largest_book, largest_chapter))
print('\n')           