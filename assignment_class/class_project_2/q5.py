# 5. Library Management System
# Problem

# Design a library system.

# Requirements

# Each book should contain:

# book id
# title
# author
# availability status
# Functionalities
# Issue book
# Return book
# Display availability
# Count total books using class variable
# Additional Challenge

# Prevent issuing already issued books.

# Concepts Practiced
# object state changes
# boolean flags
# class variables


class Library:
    __count = 0

    def __init__(self,book_id=0,title="",author="",status=False):
        self.__title = title
        self.__author = author
        self.__book_id = book_id
        self.__status = status
        Library.__count+=1


    def issue_book(self):
        if self.__status:
            self.__status = False
            print(f"Book Issued {self.__title}")
        else:
            print("No book for issue")


    def return_book(self):
        if not self.__status:
            self.__status = True
            print(f"Book Return {self.__title}")
        else:
            print("No book for return")

    def display(self):
        print("Book Details")
        print(f"Book {self.__title}")

 
    @classmethod
    def Book_count(cls):
        print(f"Total Book : {cls.__count}")   

        
Book1 = Library(1122,"slack","kishore",True)
Book2 = Library(1124,"slackwar","rohit",True)
Book3 = Library(1123,"slackrun","kishorekumar",True)
Book1.return_book()
Book1.display()
Library.Book_count()