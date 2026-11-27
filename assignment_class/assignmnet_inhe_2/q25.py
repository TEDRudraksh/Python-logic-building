# 25. Employee Work Report System
# Problem Statement

# Different employees submit reports differently.

# Create:

# abstract class WorkReport

# Child:

# DeveloperReport
# TesterReport
# ManagerReport

from abc import ABC,abstractmethod

report = []

class WorkReport(ABC):

    @abstractmethod
    def report(self):
        pass


class DeveloperReport(WorkReport):

    def __init__(self,name):
        self.__name = name
        self.__report_sub = ""
        self.__type = 'developer'
        

    def report(self):
        print("Report")
        msg = input("Write Your Report")
        self.__report_sub = msg

    @classmethod
    def add_report(self,obj):
        report.append(obj)
        print("Report Added")


class TesterReport(WorkReport):

    def __init__(self,name):
        self.__name = name
        self.__report_sub = ""
        self.__type = 'tester'

    def report(self):
        print("Report")
        msg = input("Write Your Report")
        self.__report_sub = msg

    @classmethod
    def add_report(self,obj):
        report.append(obj)
        print("Report Added")

class ManagerReport(WorkReport):

    def __init__(self,name):
        self.__name = name
        self.__report_sub = ""
        self.__type = 'manager'       

    def report(self):
        print("Report")
        msg = input("Write Your Report")
        self.__report_sub = msg

    @classmethod
    def add_report(self,obj):
        report.append(obj)
        print("Report Added")


m = ManagerReport("Rudra")
m.report()

ManagerReport.add_report(m)