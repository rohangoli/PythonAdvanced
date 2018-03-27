#!/usr/bin/python
class Employee:
    "documentaion for Employee class"

    empCount = 0
    def __init__ (self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print("Total Number of employee: %d"%Employee.empCount)
    def displayEmployee(self):
        print("Employee Name: %s\nSalary: %d\n"%(self.name,self.salary))
    def __del__(self):
        class_name = self.__class__.__name__
        print (class_name, "destroyed")

emp1=Employee("rohan",1000)
emp2=Employee("goli",1500)

emp1.name
emp2.salary

emp2.displayCount()
emp2.displayEmployee()

#hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
#getattr(emp1, 'name')    # Returns value of 'age' attribute
#setattr(emp1, 'salary', 8) # Set attribute 'age' at 8
#delattr(empl, 'salary')    # Delete attribute 'age'

#emp1.displayEmployee()


print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)

class TCS(Employee):
    "Documentation for TCS Employee"

    empCount=0
    def __init__(self):
        print("Calling TCS Class")
        
