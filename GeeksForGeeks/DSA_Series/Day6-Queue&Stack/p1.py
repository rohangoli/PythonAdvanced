#Function to check if brackets are balanced or not.
def ispar(x):
    # code here
    tempS = []
    for char in x:
        if char==']' and tempS and tempS[-1]=='[':
            tempS.pop()
        elif char==')' and tempS and tempS[-1]=='(':
            tempS.pop()
        elif char=='}' and tempS and tempS[-1]=='{':
            tempS.pop()
        else:
            tempS.append(char)
            
    if tempS==[]:
        return True
    else:
        return False