# 3. Write a program to create a class called "Rectangle" with width and height attributes. 
# Calculate the area and perimeter of the rectangle.


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
        print("PERIMETER")
        print(2*(self.__width+self.__length))
calculation = Rectangle()
calculation.set_details()
calculation.compute()