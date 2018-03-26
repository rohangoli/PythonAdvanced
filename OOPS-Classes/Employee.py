#!/usr/bin/python
class Employee:
    "Employee class"

    empCount = 0
    def __init__ (self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print("Total Number of employee: %d"%Employee.empCount)
    def displayEmployee(self):
        print("Employee Name: %s\nSalary: %d\n"%(self.name,self.salary))
