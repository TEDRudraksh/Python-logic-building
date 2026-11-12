# 15. Cricket Team Management
# Problem

# Create player management system.

# Requirements

# Each player:

# name
# role
# runs scored
# Functionalities
# Update runs
# Display statistics
# Maintain total players
# Additional Challenge

# Find highest scorer among all players.


class Cricket:

    __count = 0
    __stats = []

    def __init__(self,name="",role="",run=0):
        self.__name=name
        self.__role = role
        self.__run = run

        Cricket.__stats.append(self.__run)

        Cricket.__count+=1


    def update_run(self,run):
        Cricket.__stats.remove(self.__run)
        self.__run = run
        Cricket.__stats.append(self.__run)
        print("Run Updated Successfully")


    def display_Stats(self):
        print("Stats Details")
        print(f"Avg Run : {sum(Cricket.__stats)/len(Cricket.__stats)}")
        print(f"Highest Run : {max(Cricket.__stats)}")
        print(f"Lowest Run : {min(Cricket.__stats)}")


    @classmethod
    def Cricketer_count(cls):
        print(f"Total Crickter : {cls.__count}")   

        
pat1 = Cricket("Rudraksh","Bowler",30)
pat2 = Cricket("rohit","All rounder",50)
pat3 = Cricket("Rudra","Batter",80)
pat1.display_Stats()
Cricket.Cricketer_count()
