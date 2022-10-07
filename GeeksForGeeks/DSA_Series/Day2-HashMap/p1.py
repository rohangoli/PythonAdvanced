## Print Non-Repeated Elements In-Order of Appearance

from collections import Counter
def printNonRepeated(arr,n):
    #Your code here
    tempHM = Counter(arr)
    results = []
    for x in arr:
        if tempHM[x]==1:
            results.append(x)
    # for k,v in tempHM.items():
    #     if v==1:
    #         results.append(k)
            
    return results

test_cases = [([1,1,2,2,3,3,4,5,6,7],10),([10,20,40,30,10],5),([0,9,2,3,4,8,7],7)]
for x,y in test_cases:
    print(printNonRepeated(x,y))