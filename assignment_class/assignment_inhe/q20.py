# 20. Gaming Characters
# Character
# Warrior
# SuperWarrior

# Add special powers.

class Character:
    def __init__(self,name,health,power):
        self.__name = name
        self.__health = health
        self.__power = power

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_power(self):
        return self.__power

class Warrior(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.__tool = ""

    def rank(self):
        if Character.get_power(self)>40:
            print("You are Warrior")
            
        else:
            print("You are Soldier")

    def upgrade(self):
        if Character.get_power(self)>40:
            print("You Get tool : Sword")
            print("Your Stats are Improved")
            self.__tool = "Sword"
        else:
            print("Your Stat is too low")


class SuperWarrior(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.__tool = ""

    def rank(self):
        if Character.get_power(self)>60:
            print("You are SuperWarrior")
        elif Character.get_power(self)>40:
            print("You are Warrior")
        else:
            print("You are Soldier")

    def upgrade(self):
        if Character.get_power(self)>60:
            print("You Get tool : EnchantSword")
            print("Your Stats are Improved")
            self.__tool = "EnchantSword"
        else:
            print("Your Stat is too low")

w = SuperWarrior("Rud",100,70)
w.rank()
w.upgrade()
