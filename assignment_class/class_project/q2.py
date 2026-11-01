
# Book Library
# Create a class Book with fields: title, author, and price.
# Use setters to assign values and a method to print book details.

class Book_Library:
    def __init__(self,title=None,author=None,price=None):
        self.__title = title
        self.__author = author
        self.__price = price

    def set_book_details(self):
        title = (input("enter book title : "))
        self.__title = title

        author = (input("enter book author name : "))
        self.__author = author

        price = int(input("enter book price : "))
        self.__price = price

    def get_book_details(self):
        print("Book Details")
        print(f" title : {self.__title}")
        print(f" author name : {self.__author}")
        print(f" price : {self.__price}")


Book = Book_Library()
Book.set_book_details()
Book.get_book_details()