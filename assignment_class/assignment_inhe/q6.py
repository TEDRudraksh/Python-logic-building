# 6. Hospital Management

# Parent:

# HospitalStaff

# Child:

# Doctor
# Nurse
# Receptionist

# Implement duties().


from abc import ABC,abstractmethod
class HospitalStaff(ABC):
    @abstractmethod
    def duties(self):
        pass


class Doctor(HospitalStaff):
    def duties(self):
        print("Prescribe Dignose")


class Nurse(HospitalStaff):

    def duties(self):
        print("Take Care of Patients")


class Receptionist(HospitalStaff):

    def duties(self):
        print("Handle Admission of Patients")


r = Receptionist()
r.duties()