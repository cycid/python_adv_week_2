import Library, reader, book
user=reader.Reader("Petro")
book1=book.Book(1,"Hobbit","Tolkien", 1976,user)
library1=Library.Library("city_lib")
library1.add_book(book1)
book2=book.Book(2,"Lord of the Rings", "Tolkien", 1960, "lib")
library1.add_book(book2)
print(user)
library1.sort("name")
