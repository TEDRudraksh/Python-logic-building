
# Student Result Checker
# Create a class Student with fields: name, mathMarks, scienceMarks.
# Use setters to assign values. Add a method getAverage().



class Student:
    def __init__(self,name="", mathmarks=0, scienceMarks=0):
        self.__name = name
        self.__mathmarks = mathmarks
        self.__scienceMarks = scienceMarks

    def set_details(self):
        name = (input("Enter Name : "))
        self.__name = name

        mathmarks = int(input("Enter mathmarks : "))
        if mathmarks>=0 and mathmarks<=100:
            self.__mathmarks = mathmarks
        else:
            print("Invalid Marks")
            return False

        scienceMarks = int(input("Enter scienceMarks : "))
        if scienceMarks>=0 and mathmarks<=100:
            self.__scienceMarks = scienceMarks
        else:
            print("Invalid Marks")
            return False
      
    def getAVG(self):
        total = (self.__mathmarks+self.__scienceMarks)/2
        print(f" total {total}")

Study = Student()
Study.set_details()
Study.getAVG()