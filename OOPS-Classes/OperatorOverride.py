#!/usr/bin/python

class Vector:
    "Vector Addition"

    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return "Vector(%s,%s)"%(self.a,self.b))
    def __add__(self,other):
        return Vector(self.a+other.a,self.b+other.b)

V1=Vector(2,3)
V2=Vector(-1,4)

print(V1+V2)
