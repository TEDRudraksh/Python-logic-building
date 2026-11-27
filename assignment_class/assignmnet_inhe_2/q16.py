# 16. Hospital Billing System
# Problem Statement

# Hospital charges differ by patient type.

# Create:

# abstract class Patient

# Child:

# GeneralPatient
# ICUPatient
# EmergencyPatient

from abc import ABC,abstractmethod
class Patient(ABC):

    @abstractmethod
    def charge(self):
        pass


class General(Patient):

    def __init__(self,name,age,days):
        self.__name = name
        self.__age = age
        self.__days = days
        self.__charge = 500


    def charge(self):
        print("Your Hospital Charge - General")
        print(self.__days*self.__charge)    


class ICUPatient(Patient):

    def __init__(self,name,age,days):
        self.__name = name
        self.__age = age
        self.__days = days
        self.__charge = 1000


    def charge(self):
        print("Your Hospital Charge - ICU")
        print(self.__days*self.__charge)   



class EmergencyPatient(Patient):

    def __init__(self,name,age,days):
        self.__name = name
        self.__age = age
        self.__days = days
        self.__charge = 2000


    def charge(self):
        print("Your Hospital Charge - Emergency")
        print(self.__days*self.__charge)   


e = EmergencyPatient("Rudra",25,6)
e.charge()
