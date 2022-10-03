def solution(sequence):
    i=1
    count = 0
    tempIdx = -1
    while i<len(sequence):
        if sequence[i-1]>=sequence[i]:
            count+=1
            tempIdx = i
        i+=1
    
    if count>1:
        return False
    if count==0:
        return True
        
    if tempIdx==1 or tempIdx==len(sequence)-1:
        return True
        
    if sequence[tempIdx-1]<sequence[tempIdx+1]:
        return True
        
    if sequence[tempIdx-2] < sequence[tempIdx]:
        return True
        
    return False
    