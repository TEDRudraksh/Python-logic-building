
# 9. Library Management

# Parent:

# LibraryItem

# Derived:

# Book
# Magazine
# Newspaper

# Implement borrowing system.

from abc import ABC,abstractmethod
from datetime import date
class LibaryItem(ABC):
    @abstractmethod
    def borrow(self):
        pass

    def return_back(self):
        pass

class Book(LibaryItem):

    def __init__(self,name):
        self.__name = name
        self.__borrow_date = 0
        self.__status = False
        self.__return_date = 0
        
    def borrow(self):
        if not self.__status:
            self.__borrow_date = date.today()
            self.__status = True
            print("Borrow Success")
        else:
            print("No book for borrow")

    def return_back(self):
        if self.__status:
            self.__return_date = date.today()
            self.__status = False
            print("Book return")
        else:
            print("NO book for return")



class Magazine(LibaryItem):

    def __init__(self,name):
        self.__name = name
        self.__borrow_date = 0
        self.__status = False
        self.__return_date = 0
        
    def borrow(self):
        if not self.__status:
            self.__borrow_date = date.today()
            self.__status = True
            print("Borrow Success")
        else:
            print("No Mangzine for borrow")

    def return_back(self):
        if self.__status:
            self.__return_date = date.today()
            self.__status = False
            print("Book return")
        else:
            print("NO Mangzine for return")



class Newspaper(LibaryItem):

    def __init__(self,name):
        self.__name = name
        self.__borrow_date = 0
        self.__status = False
        self.__return_date = 0
        
    def borrow(self):
        if not self.__status:
            self.__borrow_date = date.today()
            self.__status = True
            print("Borrow Success")
        else:
            print("No Newspaper for borrow")

    def return_back(self):
        if self.__status:
            self.__return_date = date.today()
            self.__status = False
            print("Book return")
        else:
            print("NO Newspapaer for return")

n = Newspaper("Time")
n.return_back()
n.borrow()
n.return_back()