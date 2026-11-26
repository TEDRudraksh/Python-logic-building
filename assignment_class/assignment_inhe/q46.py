# 46. Hotel Booking System

# Implement:

# room types
# booking
# pricing


class Hotel:

    def __init__(self,name,location):
        self.__name = name
        self.__location = location


    @property
    def get_name(self):
        return self.__name

    @property
    def get_location(self):
        return self.__location


class Room(Hotel):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.__type = ["single bed","double bed"]
        self.__selcet = ""


    def room_select(self):
        print("Select your Room type")
        for i in range(len(self.__type)):
            print(self.__type[i])

        else:
            choice = input("Enter Your choice").lower()
            if choice in self.__type:
                print(f"Room Selected - {choice}")
                self.__selcet = choice
            else:
                print("No more of this type")
    @property
    def selected_room(self):
        return self.__selcet
    
class Pricing(Room):

    def __init__(self, name, location):
        super().__init__(name, location)
        self.__price = 0
        

    def price(self):
        print("Your Rent")
        if self.selected_room == "single bed":
            self.__price = 1000
            print(self.__price)

        elif self.selected_room == "double bed":
            self.__price = 1800
            print(self.__price)

        else:
            print("Invalid room type")


p = Pricing("Blue","160")
p.room_select()
p.price()
