# 27. Game Character Attack System
# Problem Statement

# Game characters attack differently.

# Create:

# abstract class Character

# Child:

# Archer
# Warrior
# Mage

from abc import ABC,abstractmethod


class Character(ABC):

    def weapon(self):
        pass



class Warrior(Character):

    def __init__(self):
        self.__weapon = "Sword"

    def weapon(self):
        print("Your Weapon")
        print(self.__weapon)

class Archer(Character):

    def __init__(self):
        self.__weapon = "Bow"

    def weapon(self):
        print("Your Weapon")
        print(self.__weapon)

class Mage(Character):

    def __init__(self):
        self.__weapon = "Ward"

    def weapon(self):
        print("Your Weapon")
        print(self.__weapon)



m = Mage()
m.weapon()