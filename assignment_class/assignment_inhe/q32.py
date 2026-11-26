# 32. Database Interface

# Methods:

# connect()
# disconnect()

# Implement:

# MySQL
# MongoDB
# PostgreSQL


from abc import ABC,abstractmethod


class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass



class MySql(Database):

    @staticmethod
    def connect(func):
        def wrapper(self):
            print("DB connected")
            r = func(self)
            return r
        return wrapper


    def disconnect(self):
        print("DB disconnected")

    @connect
    def operation(self):
        print("Mysql update is done")
        self.disconnect()




class MongoDB(Database):

    @staticmethod
    def connect(func):
        def wrapper(self):
            print("DB connected")
            r = func(self)
            return r
        return wrapper


    def disconnect(self):
        print("DB disconnected")

    @connect
    def operation(self):
        print("MongoDB update is done")
        self.disconnect()



class PostgreSQL(Database):

    @staticmethod
    def connect(func):
        def wrapper(self):
            print("DB connected")
            r = func(self)
            return r
        return wrapper


    def disconnect(self):
        print("DB disconnected")

    @connect
    def operation(self):
        print("PostgreSQL update is done")
        self.disconnect()




print("1 for MySql")
print("2 for MongoDb")
print("3 for PostgreSQL\nEnter choice : ")
choice = int(input())
db = None
if choice == 1:
    db = MySql()
    
elif choice == 2:
    db = MongoDB()
    
elif choice == 3:
    db= PostgreSQL()

db.operation()