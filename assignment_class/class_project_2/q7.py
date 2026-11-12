# 7. Hospital Patient Record System
# Problem

# Create a patient management system.

# Requirements

# Each patient should contain:

# patient id
# name
# disease
# doctor assigned
# Functionalities
# Display patient details
# Change doctor
# Count total patients admitted
# Additional Task

# Create patient from formatted string using class method.


class Hospital:

    __count = 0

    def __init__(self,name="",patient_id="",disease="",doctor=""):
        self.__name=name
        self.__patient_id = patient_id
        self.__disease = disease
        self.__doctor = doctor

        Hospital.__count+=1


    def change_doctor(self,name):
        self.__doctor = name
        print("Name Change Successfully")


    def display(self):
        print("Patinet Details")
        print(f"Name {self.__name}")
        print(f"Patient ID {self.__patient_id}")
        print(f"Disease {self.__disease}")
        print(f"Doctor :{self.__doctor}")

  
    @classmethod
    def patient_count(cls):
        print(f"Total pateint : {cls.__count}")   

        
pat1 = Hospital("Rudraksh",100,"tumor","Rishabh")
pat2 = Hospital("rohit",102,"parkinson","Rishabh")
pat3 = Hospital("Rudra",101,"cancer","Rishabh")
pat1.display()
pat1.change_doctor("Rohit")
pat1.display()
Hospital.patient_count()



