from fractions import Fraction
import datetime
# a simple class
class Employee:
    #our class variables 
    raise_amout = 1.04
    num_emps = 0
    #constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #create attribute out of others. 
        self.email = first + "." + last + "@company.com"
        Employee.num_emps += 1
    #display full name (regular method)
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    def payChange(self):
        return int(self.pay * self.raise_amout)
    def changeFraction(self):
        #must look more at fractions
        return Fraction(self.pay, self.payChange)
    #class method @classmethod: tested on raise amount
    @classmethod
    def set_raise_amount(myClass, amount):
        myClass.raise_amout = amount
    #alternative to constructor
    @classmethod
    def from_string(myClass, emp_str):
        first, last, pay = emp_str.split("-")
        return myClass(first, last, pay)
        #works well with extracting data from dates. 
    
    #static methods
    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True
#Inheritance: a developer and a manager class with Employee class attributes. 
class Developer(Employee):
    def __init__(self, first, last, pay, skill):
        #handling parent variables. 
        super().__init__(first, last, pay)
        #unique attribute
        self.skill = skill
    def hello(self):
        print("hello")
class Manager(Employee):
    #constructor
    def __init__(self, first, last, pay, employees=None):
        #inherited attributes. 
        super().__init__(first, last, pay)
        #unique attribute: employee under management
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

        #method to add employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

        #print employess
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullName())

        

emp_1 = Employee("James", "Franco", 7000)
emp_2 = Employee("Marc", "Zucker", 9000)
print(emp_1.email)
print(emp_1.fullName() + " can be reached at " + emp_1.email)
#testing class method
Employee.set_raise_amount(1.10)
print(emp_1.payChange())

#instance data
    #print(emp_1.__dict__)



#testing def from_string
emp_str_3 = "John-Doe-200"
emp_3 = Employee.from_string(emp_str_3)
print(emp_3.fullName())
my_date = datetime.date(2023, 9, 18)
print(Employee.is_work_day(my_date))

#create one dev and manager
dev1 = Developer("Martin", "Zimula", 200, "Python")
mng1 = Manager("Mette", "Daniels", 400, [dev1])
print(dev1.email)
print(mng1.email)
print(Employee.num_emps, "employees at the moment")
print(dev1.skill)
print(mng1.email)
#assign more employees
mng1.add_emp(emp_1)
mng1.print_emps()