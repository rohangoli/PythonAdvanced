## https://www.geeksforgeeks.org/the-stock-span-problem/

from cgi import test
from typing import List

def stockSpan(nums):

    result = [1]*len(nums)

    tempS = [0]
    i=1
    while i<len(nums):
        while tempS and nums[tempS[-1]] <= nums[i]:
            tempS.pop()
        print(tempS)
        result[i]= i+1 if not tempS else (i-tempS[-1])
        tempS.append(i)
        i+=1

    return result

test_cases = [[10,4,5,90,120,80],[100,80,60,70,60,75,85]]
for tc in test_cases:
    print(stockSpan(tc))