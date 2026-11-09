# 5. Write a  program to create a class called "Book" with attributes for title, author, and ISBN, and
#  methods to add and remove books from a collection.

class Book:
    def __init__(self,title=None,author=None,isbn=None):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__books = []


    def add_book(self):
        title = (input("enter book title : "))
        self.__title = title

        author = (input("enter book author name : "))
        self.__author = author

        isbn = int(input("enter ISBN : "))
        self.__isbn = isbn

        dic = {"title":self.__title,"author":self.__author,"isbn":self.__isbn}
        self.__books.append(dic)
        print("Book Added")

    def remove_book(self):
        isbn = int(input("enter ISBN : "))
        for book in self.__books:
            if book["isbn"] == isbn:
                self.__books.remove(book)
                print("Book Removed")

    def display(self):
        print(self.__books)

        
Book1 = Book()
Book1.add_book()
Book1.display()
Book1.add_book()
Book1.display()
Book1.remove_book()
Book1.display()