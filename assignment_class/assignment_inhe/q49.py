# 49. Movie Streaming Platform

# Features:

# movies
# subscriptions
# watch history

# Use abstract subscription plans.

movie_list = []
history = []

from abc import ABC,abstractmethod
class Subscriptions(ABC):

    @abstractmethod
    def plan(self):
        pass


class WatchHistory:

    def watch_history(self):

        print("Movie You watch till now")
        for i in history:
            print(i)


class Movies(Subscriptions,WatchHistory):

    def __init__(self,name):
        self.__name = name
        self.__plan = False

    @classmethod
    def add_movie(cls,obj):
        movie_list.append(obj)

    def plan(self):
        print("Plan Subscribe You can now watch movie")
        self.__plan = True

    def movie(self):
        return self.__name
        
    def play_movie(self):
        if self.__plan == True:
            for i in movie_list:
                print(i.movie())

            else:
                choice = input("Enter which movie you want to watch")
                for i in movie_list:
                    if i.movie() == choice:
                        print(f"You are Watching - {choice}")
                        history.append(choice)
                        break
                else:
                    print("Invalid input/not in list")
        else:
            print("Subscribe First")


m1 = Movies("Avengers")
m2 = Movies("hera pehri")
m3 = Movies("dark lord")



Movies.add_movie(m1)
Movies.add_movie(m2)
Movies.add_movie(m3)


m1.plan()
m1.play_movie()
m1.watch_history()