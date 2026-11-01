# Movie Rating System
# Create a class Movie with fields: name, genre, and rating.
# Use setters and create a method isHit() that returns true if rating ≥ 8.0.



class Movie:
    def __init__(self,name=None,genre=None, rating=None):
        self.__name = name
        self.__genre = genre
        self.__rating = rating

    def set_details(self):
        name = (input("Enter name : "))
        self.__name=  name 

        genre = (input("Enter genre : "))
        self.__genre = genre

        rating = float(input("Enter rating : "))
        self.__rating = rating

    def isHit(self):
        if self.__rating>=8.0:
            return True
        else:
            return False


film = Movie()
film.set_details()
print(f"HIT : {film.isHit()}")