## Minimum Number

import heapq

def minimumNumber(n, arr):
    #code here
    for _ in range(n):
        ## Approach 2:
        max1 = 0
        i=0
        while i<n:
            if arr[i]>arr[max1]:
                max1=i
            i+=1
        max2 = 0
        i=0
        while i<n:
            if arr[max2]<arr[i]<arr[max1]:
                max2=i
            i+=1
        
        print(max1, max2)
        if max1!=max2:
            arr[max1] = arr[max1]-arr[max2]

        ## Approach1:
        # (i,j) = heapq.nlargest(2, range(len(arr)), key=arr.__getitem__)
        # arr[i] = arr[i]-arr[j]

        print(arr)
    return max(arr)

print('Case1:')
print([3,2,4])
print(minimumNumber(3,[3,2,4])) ## 1 [3,2,4] -> [3,2,1] -> [1,2,1] -> [1,1,1]

print('Case2:')
print(minimumNumber(2,[2,4])) ## 2 [2,4] -> [2,2] -> [2,0]
