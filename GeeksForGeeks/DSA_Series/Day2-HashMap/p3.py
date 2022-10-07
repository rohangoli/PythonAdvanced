## Sort an array according to the other - Relative Sort

def relativeSort (A1, N, A2, M):
    # Your Code Here
    def binary_search(arr,start,end,target):
        if end>=start:
            mid = (end+start)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]<target:
                return binary_search(arr,mid+1,end,target)
            else:
                return binary_search(arr,start,mid,target)
        return -1

    def first_occurence(arr,start,end,target):
        if end>=start:
            mid = start + (end-start)//2
            if((mid==0 or target>arr[mid-1]) and arr[mid]==target):
                return mid
            elif arr[mid]<target:
                return first_occurence(arr,mid+1,end,target)
            else:
                return first_occurence(arr,start,mid-1,target)
        return -1

    ## Temp Sorted Array
    temp = sorted(A1)
    
    ## Mark the entries
    visited = [False]*N
    
    ## Copy Sorted Elements only present in A2
    idx = 0
    j = 0
    while j<m:
        pos = first_occurence(temp,0,N-1,A2[j])
        if pos==-1:
            j+=1
            continue
        
        i=pos
        while(i<N and temp[i]==A2[j]):
            A1[idx] = temp[i]
            idx+=1
            visited[i]=True
            i+=1
        
        j+=1

    ## Copy Remaining Elements 
    i=0
    while i<N:
        if not visited[i]:
            A1[idx] = temp[i]
            idx+=1
        i+=1
        
    return A1

test_cases = [
    ([2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8],11,[2,1,8,3],4),
    ([2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8],11,[99, 22, 444, 56],4)]

import signal

def signal_handler(signum, frame):
    raise Exception("Timed out!")

signal.signal(signal.SIGALRM, signal_handler)
signal.alarm(10)   # Ten seconds

for a1,n,a2,m in test_cases:
    try:
        print(relativeSort(a1,n,a2,m))
    except Exception as msg:
        print("Timed out!")
    