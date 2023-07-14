## Smaller Sum

def smallerSum(n : int, arr : List[int]) -> List[int]:
    # code here
    
    result = []
    i=0
    while i<n:
        j=0
        tempSum = 0
        while j<n:
            if arr[j]<arr[i]:
                tempSum+=arr[j]
            j+=1
        result.append(tempSum)
        i+=1
    
    # tempH = [0]
    
    # def bin_search(nums, target):
    #     start=0
    #     end=len(nums)-1
    #     while start<=end:
    #         mid = start + (end-start)//2
    #         if nums[mid]<=target:
    #             start=mid+1
    #         else:
    #             end=mid-1
    #     return end
    
    # i=0
    # result=[]
    # while i<n:
    #     heapq.heappush(tempH,-1*arr[i])
    #     pos = bin_search(tempH, -1*arr[i])
    #     result.append(-1*sum(tempH[pos+1:]))
    #     i+=1
        
    return result
