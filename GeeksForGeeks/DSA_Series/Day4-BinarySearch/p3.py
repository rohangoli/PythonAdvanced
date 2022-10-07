## Counting elements in two arrays

def countEleLessThanOrEqual(arr1,n1,arr2,n2):
    #returns the required output
    
    arr2.sort()
    #print(arr2)
    
    ## Find last Occurence of Number
    def binary_search(arr,n, x):
        start = 0
        end = n-1
        while start<=end:
            mid = start + (end-start)//2
            if arr[mid]<=x:
                start = mid+1
            else:
                end = mid-1
                
        return end
    
    i=0
    result = []
    while i<n1:
        last_pos = binary_search(arr2, n2, arr1[i])
        result.append(last_pos+1)
        i+=1
        
    return result
    
## TLE
def countEleLessThanOrEqual_OLD(arr1,n1,arr2,n2):
    #returns the required output
    
    arr2.sort()
    #print(arr2)
    
    def binary_search(arr, start, end, target):
        if end>=start:
            mid = start + (end-start)//2
            if (mid==0 or target>arr[mid-1]) and arr[mid]==target:
                return mid
            elif target>arr[mid]:
                return binary_search(arr,mid+1,end,target)
            else:
                return binary_search(arr, start, mid-1, target)
                
        return -1        
    
    i=0
    result = []
    while i<n1:
        first_pos = binary_search(arr2, 0 , n2-1, arr1[i])
        if first_pos==-1 and i==0:
            result.append(0)
        elif first_pos==-1:
            result.append(result[-1])
        else:
            last_pos = first_pos
            while last_pos<n2 and arr2[last_pos]==arr1[i]:
                last_pos+=1
            last_pos-=1
            #print(arr1[i], last_pos)
            result.append(last_pos+1)
        i+=1
        
    return result