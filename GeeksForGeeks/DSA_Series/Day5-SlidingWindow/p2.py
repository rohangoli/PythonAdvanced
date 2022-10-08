## Count Distinct elements in every windows

from collections import Counter

def countDistinct(A, N, K):
    # Code here
    result = []
    
    ## TLE
    # tempHM = Counter()
    # i=0
    # begin = 0
    # while i<n:
    #     tempHM[A[i]]+=1
    #     if i-begin>K:
    #         tempHM[A[begin]]-=1
    #         if tempHM[A[begin]]==0:
    #             del tempHM[A[begin]]
    #         begin+=1
    #     result.append(len(tempHM.keys()))
    #     i+=1
    
    i=0
    begin=0
    while (i+K-1)<N:
        if i==0:
            tempHM = Counter(A[i:i+K])
        else:
            tempHM[A[i+K-1]]+=1
            tempHM[A[begin]]-=1
            if tempHM[A[begin]]==0:
                del tempHM[A[begin]]
            begin+=1
        #print(tempHM)
        result.append(len(tempHM.keys()))
        i+=1
    return result