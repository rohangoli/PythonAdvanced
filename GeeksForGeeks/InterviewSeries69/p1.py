from collections import defaultdict
from typing import List

def solveQueries(N : int, num : int, A : List[int], Q : List[List[int]]) -> List[int]:
    # code here
    freqArr=[0]*len(A)
    freqHM=defaultdict(lambda:0)
    i=len(A)-1
    while i>-1:
        freqHM[A[i]]+=1
        freqArr[i] = freqHM[A[i]]
        i-=1

    # print(freqHM)
    # print(freqArr)
    result = []
    for idx in range(num):
        temp=0
        (start,end,goal)=Q[idx]
        print(start,end,goal)
        for x in freqArr[start:end+1]:
            print(freqArr[start:end+1],x,goal, x==goal)
            if x==goal:
                temp+=1
        result.append(temp)
    print('-'*15)
    return result

print('TC1:')
print(solveQueries(5,4,[1,1,3,4,3],[[0,2,2],[0,2,1],[0,4,2],[0,4,3]]))

print('TC2:')
print(solveQueries(5,2,[1,1,1,1,1],[[0,4,4],[0,4,5]]))