class Book:
    title = ""
    isbn = None
    genre = None
    author = None

b1 = Book()
b1.title = "Star Wars"
b1.isbn = 1234567
b1.genre = "Scifi"
b1.author = "G. Lucas"

b2 = Book()
b2.title = "Blade Runner"
b2.isbn = 2345678
b2.genre = "Scifi"
b2.author = "Dude"


# my_book_list = [b1, b2]
#
# for b in my_book_list:
#     print("Book ISBN {}, Name {}".format(b.isbn, b.title))