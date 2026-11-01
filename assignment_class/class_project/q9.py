# Circle Geometry
# Create a class Circle with field radius.
# Use a setter to assign radius. Add methods to compute area and circumference.

class Circle:
    def __init__(self,radius=0):
        self.__radius = radius

 

    def set_details(self):
        radius = int(input("radius : "))
        self.__radius = radius

        
    def compute(self):
        print("AREA")
        print(3.14*(self.__radius*self.__radius))

        print("CIRCUMFERENCE")
        print(round(2*3.14*self.__radius))

calculation = Circle()
calculation.set_details()
calculation.compute()