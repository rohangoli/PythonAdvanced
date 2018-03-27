class Parent:
    "Parent Class docs"

    name = ""
    salary = 0
    
    def __init__(self):
        #Parent Class Constructor
        print("Parent Class Constructor")

    def setAttr(self,name,salary):
        Parent.name=name
        Parent.salary=salary

    def getAttr(self):
        print("Name:%s\nSalary:%d\n"%(Parent.name,Parent.salary))

class Child(Parent):
    "Child Class docs"

    def __init__(self):
        print("Child Class Constructor")

    #Method Override
    def getAttr(self):
        print("Name:%s\n"%(Parent.name))
        
p=Parent()
p.setAttr("rohan",24000)
p.getAttr()

q=Child()
q.setAttr("goli",2000)
q.getAttr()
