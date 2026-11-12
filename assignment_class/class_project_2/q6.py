# 6. Movie Ticket Booking System
# Problem

# Create a movie booking system.

# Requirements

# Each movie should have:

# movie name
# total seats
# available seats
# Functionalities
# Book tickets
# Cancel tickets
# Prevent overbooking
# Display seat availability
# Concepts Practiced
# state updates
# validations
# object behavior



class Movie:

    def __init__(self,name="",total_seats="",availabe_seats=""):
        self.__name=name
        self.__total_seats = total_seats
        self.__availabe_seats = availabe_seats
        self.__buy = False

    def book_ticket(self,no):
        if self.__availabe_seats>no:
            self.__availabe_seats-=no
            self.__buy = True
            self.__buyno = no
            print(f"Booked Ticket")
        else:
            print("try with less seat")


    def cancel_ticket(self):
        if self.__buy:
            self.__availabe_seats+= self.__buyno 
            print(f"Booking Cancel")
        else:
            print("No ticket for cancel")

    def display(self):
        print("Movie Details")
        print(f"Name {self.__name}")
        print(f"Seats {self.__total_seats}")
        print(f"AvlSeats {self.__availabe_seats}")

 

        
Book1 = Movie("Avenger",100,30)
Book1.display()
Book1.book_ticket(10)
Book1.display()
Book1.cancel_ticket()
Book1.display()
