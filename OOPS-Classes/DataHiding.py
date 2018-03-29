class counter:
    "data hiding class"

    __secretcount=0

    def __init__(self):
        print("Incremented Secret Counter")
        counter.__secretcount +=1
    
c=counter()

#It works
print(c._counter__secretcount)

#it does not work
# print(c.__secretcount)
