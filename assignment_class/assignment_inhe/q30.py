# 30. Restaurant Management

# Abstract:

# Restaurant

# Derived:

# PizzaRestaurant
# BurgerRestaurant

# Prepare food differently.

from abc import ABC,abstractmethod
class Restaurant(ABC):

    @abstractmethod
    def food(self):
        pass


class PizzaRestaurant(Restaurant):

    def food(self):
        print("Your Pizza is Ready")
        print("It contain - base,topping,veggies,origano,chilli,souce etc...")


class BurgerRestaurant(Restaurant):

    def food(self):
        print("Your Burger is Ready")
        print("It contain - buns,pattiy,veggies,stuffing etc.....")



print("1 for Order Pizza")
print("2 for Order Burger\nEnter choice : ")
choice = int(input())
eat = None
if choice == 1:
    eat = PizzaRestaurant()
    
elif choice == 2:
    eat = BurgerRestaurant()
    
eat.food()