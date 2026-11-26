# 26. Media Player

# Abstract:

# MediaPlayer

# Derived:

# AudioPlayer
# VideoPlayer

# Implement play functionality.

from abc import ABC,abstractmethod
class MediaPlayer(ABC):

    @abstractmethod
    def play(self):
        pass


    @abstractmethod
    def next_(self):
        pass


class AudioPlayer(MediaPlayer):

    __count = 0

    def __init__(self,name,next):
        self.__name = name
        self.__next = next
        
    def play(self):
        if AudioPlayer.__count%2==0:
            print(f"Song is Playing : {self.__name}")
            AudioPlayer.__count+=1

        else:
            print(f"Song is Paused : {self.__name}")
            AudioPlayer.__count+=1

    def next_(self):
        print("Next Song")
        self.__name = self.__next
        AudioPlayer.__count = 0


  
class VideoPlayer(MediaPlayer):

    __count = 0

    def __init__(self,name,next):
        self.__name = name
        self.__next = next
        
    def play(self):
        if VideoPlayer.__count%2==0:
            print(f"Video is Playing : {self.__name}")
            VideoPlayer.__count+=1

        else:
            print(f"Video is Paused : {self.__name}")
            VideoPlayer.__count+=1

    def next_(self):
        print("Next Video")
        self.__name = self.__next
        VideoPlayer.__count = 0

v = VideoPlayer("GTA-6","BGMI")
v.play()
v.play()