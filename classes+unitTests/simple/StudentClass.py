'creating a simple class'
class Student:
    'adding contructor'
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)
    'adding methods to class'
    def getName(self):
        return self.name
    def getHours(self):
        return self.hours
    def getQpoint(self):
        return self.qpoints
    def gpa(self):
        return self.qpoints / self.hours







