## Substrings of length-k with k-1 distinct elements

from collections import Counter

def countOfSubstrings(S, K):
    # code here 
    tempHM = Counter()
    i=0
    begin = 0
    result = 0
    while (i+K-1)<len(S):
        #print(i,i+K)
        if i==0:
            tempHM = Counter(S[i:i+K])
        else:
            tempHM[S[i+K-1]]+=1
            tempHM[S[begin]]-=1
            if tempHM[S[begin]]==0:
                del tempHM[S[begin]]
            begin+=1
        
        #print(tempHM)
        if len(tempHM.keys())==K-1:
            result+=1
        
        i+=1
        
    return result