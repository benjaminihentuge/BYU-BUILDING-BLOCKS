
largest_chapter = 0
largest_BOM_chapter = 0
view = ''

view = input('Do you want to view the Life Expectancy Stats')
 
while True:
    if view == 'yes':
        print('\n')
        with open('books_and_chapters.txt') as standard_works:
            for books in standard_works:
                books = books.strip()
                books = books.split(':')

                book = books[0]
                chapters = int(books[1])
                scripture = books[2]

                
                
                if chapters > largest_chapter:
                    largest_chapter = chapters
                    largest_book = book



                # Stretch 1
                if scripture == 'Book of Mormon':
                    if chapters > largest_BOM_chapter:
                        largest_BOM_chapter = chapters
                        largest_BOM_book = book


                        
                # Stretch 2
            print('The book with the largest number of chapters in the Book 0f Mormon is {} with {} chapters.'.format(largest_BOM_book, largest_BOM_chapter))       

            #print('The book with the largest number of chapters in the scripture is {} with {} chapters.'.format(largest_book, largest_chapter))
        print('\n')

                #Stretch3
        print('\n')

        choice = input('What volume of scripture would you love to learn about? ' )
        print('')
        largest_chapter = 0


        with open('books_and_chapters.txt') as standard_works:
            for books in standard_works:
                books = books.strip()
                books = books.split(':')

                book = books[0]
                chapters = int(books[1])
                scripture = books[2]



                if scripture.lower() == choice.lower():
                    if chapters > largest_chapter:

                        largest_chapter = chapters
                        largest_book = book
                        


            print('The book with the largest number of chapters in the {} is {} with {} chapters.'.format(choice, largest_book, largest_chapter))
        print('\n')      

    elif view != 'yes':
        print('Thanks for visiting this site')
        