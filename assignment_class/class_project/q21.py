
# 11. Write a program to create a class called "Library" with a collection of books and methods to add and remove books.

class Library:
    def __init__(self,collection=[]):
        self.__collection = collection

    def add_book(self):
        book = input("Enter Book to Add : ")
        self.__collection.append(book)
        print("Book Added")

    def remove_book(self):
        rm_book = input("Enter Book to Remove : ")
        if rm_book in self.__collection:
            self.__collection.remove(rm_book)
        else:
            print("Not in collection")

    def display(self):
        print(f"Collection : {self.__collection}")

collect = Library()
collect.display()
collect.add_book()
collect.display()
collect.remove_book()
collect.display()