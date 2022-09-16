## Minimum Number

import heapq as hq

def minimumNumber(n, arr):
    #code here
    if len(arr)==1:
        return arr[0]
    ## Approach3 - TLE
    arr2 = [x*-1 for x in arr]
    for _ in range(n):
        hq.heapify(arr2)
        fMax = hq.heappop(arr2)
        hq.heapify(arr2)
        sMax = arr2[0]
        hq.heappush(arr2, fMax-sMax)
        print(arr2)
    return min(arr2)*-1
    
    # for _ in range(n):
        ## Approach 2:
        # max1 = 0
        # i=0
        # while i<n:
        #     if arr[i]>arr[max1]:
        #         max1=i
        #     i+=1
        # max2 = 0
        # i=0
        # while i<n:
        #     if arr[max2]<arr[i] and max2!=max1:
        #         max2=i
        #     i+=1
        
        # print(max1, max2)
        # arr[max1] = arr[max1]-arr[max2]
        # print(arr)

        ## Approach1:
        # (i,j) = heapq.nlargest(2, range(len(arr)), key=arr.__getitem__)
        # arr[i] = arr[i]-arr[j]

    #return max(arr)

print('Case1:')
print([3,2,4])
print(minimumNumber(3,[3,2,4])) ## 1 [3,2,4] -> [3,2,1] -> [1,2,1] -> [1,1,1] = max=1

print('Case2:')
print(minimumNumber(2,[2,4])) ## 2 [2,4] -> [2,2] -> [2,0] = max=2
