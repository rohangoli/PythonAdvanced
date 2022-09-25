from typing import List
import math
def optimalArray(n : int, a : List[int]) -> List[int]:
    # code here
    result = [0]*n
    i=1
    while i<=n:
        if i%2==0:
            median = math.ceil((a[i//2-1]+a[i//2])/2)
        else:
            median = a[i//2]
        print(i,median)
        temp = 0
        for x in a[:i]:
            temp+= abs(median-x)
        result[i-1]=temp
        i+=1
    print('-'*10)
    return result

print('TC1:')
print(optimalArray(4,[1,6,9,12]))

print('TC2:')
print(optimalArray(7,[1,1,1,7,7,10,19]))