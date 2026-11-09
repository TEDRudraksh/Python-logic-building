# 17. Write a program to create a class called "Movie" with attributes for title, director, actors, and reviews, 
# and methods for adding and retrieving reviews.


class Movie:
    def __init__(self,title="",director="",actors="",reviews = []):
        self.__title = title
        self.__director = director
        self.__actor = actors
        self.__review = reviews

    def add_info(self):
        title = input("Enter Title")
        self.__title = title

        director = input("Enter Director Name")
        self.__director = director

        actor = input("Enter Actor Name")
        self.__actor = actor

    def add_review(self):

        reviews = input("Enter Your Review : ")
        self.__review.append(reviews)

    def get_review(self):

        print(f"Review of {self.__title}")
        print(f"Review : {self.__review}")

rev = Movie()
rev.add_review()
rev.get_review()