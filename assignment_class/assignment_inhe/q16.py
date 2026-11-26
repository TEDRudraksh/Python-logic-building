# 16. E-commerce User Roles
# User
# Seller(User)
# PremiumSeller(Seller)

# Add premium benefits.

class User:
    def __init__(self,name,age):
        self.__age = age
        self.__name = name

    def details(self):
        print(self.__name,self.__age)



class Seller(User):
    def __init__(self, name, age,plan):
        super().__init__(name, age)
        self.__plan = plan

    def get_plan(self):
        return self.__plan

    def benefits(self):
        print("Service")
        print(f"Plan : {self.__plan}")
        print("Service Provided")
        print(f"Inventory Management\n Delievery\n")


class PremiumSeller(Seller):

    def __init__(self, name, age,plan):
        super().__init__(name, age,plan)

    def benefits(self):
        print("Service")
        print(f"Plan : {Seller.get_plan(self)}")
        print("Service Provided : ")
        print(f" Inventory Management\n Priority Delievery\n Store ads on website\n Top in searches")


p = PremiumSeller("Rud",25,"Premium")
p = Seller("RUU",24,"basic")
p.details()
p.benefits()

              