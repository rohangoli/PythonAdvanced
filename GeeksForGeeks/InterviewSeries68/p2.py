## Remove the balls

from typing import List
from collections import defaultdict

def finLength(N : int, color : List[int], radius : List[int]) -> int:
    # code here
    
    tempHM = defaultdict(lambda:0)
    i=0
    while i<N:
        if tempHM.get((color[i],radius[i]),0)==0:
            tempHM[(color[i],radius[i])]=1
        else:
            tempHM[(color[i],radius[i])]-=1
        i+=1
            
    return sum(tempHM.values())

N = 3
color = [2, 2, 5]
radius = [3, 3, 4]
print('Case1:')
print(finLength(N,color,radius))

N = 4
color = [1, 3, 3, 1]
radius = [2, 5, 5, 2]
print('Case2:')
print(finLength(N,color,radius))

N = 5
color = [1, 3, 3, 1, 1]
radius = [2, 5, 5, 2, 2]
print('Case3:')
print(finLength(N,color,radius))