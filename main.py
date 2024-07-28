"""
task:
Library

Create three classes:
1. Library class
Fields:
- list of books (list Books)
- list of readers (list Readers)

Methods:
- Add book
- Delete book
- Give book to reader
- Accept book from reader

- List all books
- List books in library (in stock)
- List books that are out of stock

- Sort list of books by title, author, year of publication (lambda will be a plus)

2. Book class
Fields:
- ID
- Title
- Author
- Year of publication
- ??? (this parameter is needed!!!)

3. Reader class
- ???

Methods:
???
"""


import Library, reader, book

#adding data to programm
user1=reader.Reader("Petro")
book1=book.Book(1,"Hobbit","Tolkien", 1976,user1)
library1=Library.Library("city_lib")
library1.add_book(book1)
book3=book.Book(3,"12 Rules of Life","Jordan Peterson",2018,"lib")
book2=book.Book(2,"Lord of the Rings", "Tolkien", 1960)

#add book function(takes book obj as argument)
library1.add_book(book3)
library1.add_book(book2)

#print books library have(takes param "all", "in" or any another to show all books, in library or user have it
library1.print_books("in")
print('\n')
library1.print_books('any')
print('\n')
library1.print_books("all")
print("\n")

#print books user have
library1.show_user_book(user1)

#give book to user takes 2 arguments: book and reader
library1.give_book_to_reader(book3, user1)
library1.show_user_book(user1)
print("")


#get book from user takes 1 arguments:book
library1.get_book_from_reader(book3)
library1.show_user_book(user1)
print("\n")



#sort method takes 1 argument:on which parametr you want to sort "year", "name" or "author"
library1.sort("year")



#del book function(takes book obj as argument)
library1.del_book(book3)



