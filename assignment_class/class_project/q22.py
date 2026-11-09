
# 12. Write a program to create a class called "Airplane" with a flight number, destination, 
# and departure time attributes, and methods to check flight status and delay.

from datetime import time
class Airplane:
    def __init__(self,flight_no,destination,std,atd):
        self.__flight_no = flight_no
        self.__destination = destination
        self.__std = std
        self.__atd = atd
        self.__status = ""

    def flt_status(self):
        if self.__std<=self.__atd:
            self.__status = "On Air"
            print(f"Status : {self.__status}")
        else:
            self.__status = "On Ground"

    def flt_delay(self):
        if self.__std<self.__atd:
            print(f"Delay : YES")
        elif self.__std==self.__atd:
            print(f"Delay : NO")

air = Airplane("xc100","delhi",time(10,30),time(12,30))
air.flt_status()
air.flt_delay()

 



 



 


 


 



 



 

