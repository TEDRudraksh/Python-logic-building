# 17. Online Course Platform
# Course
# ProgrammingCourse
# PythonCourse

# Add certification system.


class Course:
    def __init__(self,course,score):
        self.__coursename = course
        self.__score = score

    def course(self):
        print(self.__name)

    def score(self):
        return self.__score


class ProgrammingCourse(Course):
    def __init__(self, course,score,language):
        super().__init__(course,score)
        self.__language = language


class PythonCourse(ProgrammingCourse):

    def __init__(self, course,score,language,stuname):
        super().__init__(course,score,language)
        self.__stuname = stuname

    def certification(self):
        if self.score()>=75:
            print("Congrats On your Certification")

        else:
            print("You didnot pass the test , try again")

p = PythonCourse("Programming",25,"Python","Rud")
p.certification()
