## K sorted array

def isKSortedArray(arr, n, k): 
    #code here.
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
        
    temp = sorted(arr)
    
    i=0
    while i<n:
        find_pos = binary_search(temp,0,n-1,arr[i])
        #print(find_pos,i,arr[i])
        if abs(find_pos-i)>k:
            return "No"
        i+=1
    
    return "Yes"

test_cases = [
    ([3, 2, 1, 5, 6, 4],6,2),
    ([3, 2, 1, 5, 6, 4],6,1),
    ([13, 8, 10, 7, 15, 14, 12],7,1),
    ([13, 8, 10, 7, 15, 14, 12],7,4)
    ]
for x,y,z in test_cases:
    print(isKSortedArray(x,y,z))