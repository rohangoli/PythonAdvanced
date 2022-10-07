## First and Last Occurence of X

def find(arr,n,x):
    # code here
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
        
    first_pos = binary_search(arr, 0, n-1, x)
    if first_pos == -1:
        return -1,-1
    last_pos = first_pos
    while last_pos<n and arr[last_pos]==x:
        last_pos+=1
        
    return first_pos,last_pos-1

test_cases = [
    ([1, 3, 5, 5, 5, 5, 67, 123, 125],9,5),
    ([1, 3, 5, 5, 5, 5, 7, 123, 125],9,7),
    ([1, 3, 5, 5, 5, 5, 67, 123, 125],9,4),
    ([6,9],2,9)
    ]
for x,y,z in test_cases:
    print(find(x,y,z))