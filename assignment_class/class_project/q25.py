# 15. Write a program to create a class called "MusicLibrary" with a collection of songs and methods 
# to add and remove songs, and to play a random song.

import random

class MusicLibrary:
    def __init__(self,songs=[]):
        self.__songs = songs


    def add_song(self):
        name =input("Enter Song Name : ")
        self.__songs.append(name)
        print("Song Added")

    def rm_song(self):
        name =input("Enter song Name to Remove: ")
        for rm in range(len(self.__songs)):
            if self.__songs[rm] == name:
                self.__songs.remove(self.__songs[rm])
                print("Song Removed")
            else:
                print("Does not Exist")


    def play_random(self):
        print("Random song")
        print(random.choice(self.__songs))


play = MusicLibrary()
play.add_song()
play.add_song()
play.add_song()
play.play_random()

