# 16. Train Reservation System
# Problem

# Design ticket reservation system.

# Requirements

# Train should contain:

# train number
# total seats
# booked seats
# Functionalities
# Reserve seat
# Cancel seat
# Display available seats

class Train:

    __trains = []

    def __init__(self,train_no,total_seats,booked_seats):
        self.__train_no = train_no
        self.__total_seats = total_seats
        self.__booked_seats = booked_seats
        self.__train = []
        dic = {"train_no":train_no,"total_seats":total_seats,"booked_seats":booked_seats}
        Train.__trains.append(dic)

        
    def book_train(self,seats):
        trn_no = input("Enter Train No : ").lower()
        ok = True
        for trn in self.__trains:
            if trn["train_no"].lower() == trn_no:
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

                dic =  {"name":name,"phone":phone ,"trn_no": trn_no}
                self.__train.append(dic)
                print("Train Booked")
                ok = False
        if ok:
            print("No Train ")            


    def cancel_train(self):
        no = input("Enter train No for cancel ").lower()
        for trn in self.__train:
            if trn["trn_no"] == no:
                self.__train.remove(trn)
                self.__booked_seats-= self.__book
                
            else:
                print("Invalid Item")

    def display(self):
        print("Train Details")
        print(f"{self.__train_no} T : {self.__total_seats}  b : {self.__booked_seats}")
  


passenger = Train("12415",60,40)
passenger.display()
passenger.book_train(10)
passenger.display()
passenger.cancel_train()
passenger.display()
