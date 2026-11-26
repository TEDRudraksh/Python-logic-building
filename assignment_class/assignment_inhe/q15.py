# 15. Sports Management
# Player
# CricketPlayer
# Captain(CricketPlayer)

# Add captain-specific functionality.

class Player:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

class CricketPlayer(Player):
    def __init__(self, name, age,category):
        super().__init__(name, age)
        self.__category = category

class Captain(CricketPlayer):
    def __init__(self, name, age, category):
        super().__init__(name, age, category)
        self.__teamselect = ""
        self.__playselect = ""

    def teamselect(self,player):
        self.__teamselect+=player
        print("Team Selected")

    def playselect(self,play):
        self.__playselect+=play
        print("Play Selected if Toss Win")


c = Captain("rud",25,"batsmen")
c.teamselect("sac")
c.playselect("bat")