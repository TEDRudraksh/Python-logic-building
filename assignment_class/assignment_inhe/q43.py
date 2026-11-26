# 43. Railway Reservation System

# Classes:

# Passenger
# Ticket
# Train

# Add booking logic.

class Passenger:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age


class Train:
    def __init__(self):
        self.__trn = "12415"
        self.__seats = 100
        self.__booked = 60

    def get_trn(self):
        return self.__trn

    def get_seats(self):
        return self.__seats

    def get_booked(self):
        return self.__booked

    def set_booked(self,seat):
        self.__booked = self.__booked+ seat
        return  self.__booked


class Ticket(Passenger,Train):

    def __init__(self, name, age,boarding,destination,depdate,aridate):
        Passenger.__init__(self, name, age)
        Train.__init__(self)
        self.__boarding = boarding
        self.__destination = destination
        self.__depdate = depdate
        self.__aridate = aridate


    def booking(self,name,age,trn,seat,boarding,destination,depdate,aridate):
        print("Book Train")

        if self.get_trn() == trn:
            print(f"Name : {name}")
            print(f"Age : {age}")

            if (self.get_seats() - self.get_booked())>= seat:
                print("Your seat is booked")
                self.set_booked(seat)
                print(self.get_booked())

b = Ticket("Rudraksh",25,"Delhi","Indore","12-12-26","13-12-26")
b.booking("Rudraksh",25,"12415",5,"Delhi","Indore","12-12-26","13-12-26")
        





