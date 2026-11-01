
# Rectangle Area Calculator
# Create a class Rectangle with fields: length, width.
# Use setters to assign values. Add a method to calculate area.


class Rectangle:
    def __init__(self,length=0,width=0):
        self.__length = length
        self.__width = width

 
    def set_details(self):
        length = int(input("length : "))
        self.__length = length

        width = int(input("width : "))
        self.__width = width

        
    def compute(self):
        print("AREA")
        print(self.__width*self.__length)

calculation = Rectangle()
calculation.set_details()
calculation.compute()