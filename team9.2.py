
largest_chapter = 0
largest_BOM_chapter = 0

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
        
        



    
        print(book) 
    print('The book with the largest number of chapters in the scripture is {} with {} chapters.'.format(largest_book, largest_chapter))