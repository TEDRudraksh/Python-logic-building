# 4. Write a program to create a class called "Circle" with a radius attribute. You can access and modify this attribute. 
# Calculate the area and circumference of the circle.


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