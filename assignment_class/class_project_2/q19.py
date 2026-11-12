# 19. Flight Reservation System
# Problem

# Create airline reservation software.

# Requirements

# Flight should contain:

# flight number
# total seats
# booked seats
# Functionalities
# Book ticket
# Cancel ticket
# Prevent overbooking




class Flight:

    __flights = []

    def __init__(self,flight_no,total_seats,booked_seats):
        self.__flight_no = flight_no
        self.__total_seats = total_seats
        self.__booked_seats = booked_seats
        self.__flight = []
        dic = {"flight_no":flight_no,"total_seats":total_seats,"booked_seats":booked_seats}
        Flight.__flights.append(dic)

        
    def book_Flight(self,seats):
        flt_no = input("Enter Flight No : ").lower()
        ok = True
        for flt in self.__flights:
            if flt["flight_no"].lower() == flt_no:
                name = input("Enter Your Name : ").lower()
                self.__name = name

                phone = int(input("Enter Phone No : "))
                if len(str(phone))!=10:
                    return print("Invalid No.")
                self.__phone = phone

                if (self.__total_seats - self.__booked_seats)>seats:
                    self.__book = seats
                    self.__booked_seats+=seats
                else:
                    return print(f"only {(self.__total_seats - self.__booked_seats)} are Availabe")

                dic =  {"name":name,"phone":phone ,"flt_no": flt_no}
                self.__flight.append(dic)
                print("Flight Booked")
                ok = False
        if ok:
            print("No Flight ")            


    def cancel_Flight(self):
        no = input("Enter Flight No for cancel ").lower()
        for flt in self.__flight:
            if flt["flt_no"] == no:
                self.__flight.remove(flt)
                self.__booked_seats-= self.__book
                
            else:
                print("Invalid No")

    def display(self):
        print("Flight Details")
        print(f"{self.__flight_no} T : {self.__total_seats}  b : {self.__booked_seats}")
  


passenger = Flight("12415",60,40)
passenger.display()
passenger.book_Flight(100)
passenger.display()
passenger.cancel_Flight()
passenger.display()
