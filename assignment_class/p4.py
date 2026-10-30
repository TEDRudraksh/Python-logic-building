#time add 2 time hr,min,sec 

class Time:
    def __init__(self,hr,min,sec):
        self.__hr = hr
        self.__min = min
        self.__sec = sec

    def add(self,t1,t2):
        t3.__hr = t1.__hr + t2.__hr
        t3.__min = t1.__min + t2.__min
        t3.__sec = t1.__sec + t2.__sec

        if t3.__min>=60:
            t3.__hr+=1
            t3.__min-=60
        if t3.__sec>=60:
            t3.__min+=1
            t3.__sec-=60

    def display(self):
        print(f"{self.__hr} {self.__min} {self.__sec}")

t1 = Time(5,30,30)
t1.display()
t2 = Time(6,20,60)
t2.display()
t3 = Time(0,0,0)
t3.add(t1,t2)
t3.display()