## 2091. Removing Maximum and Minimum from Array

# Example 1:
# Input: nums = [2,10,7,5,4,1,8,6]
# Output: 5
# Explanation: 
# The minimum element in the array is nums[5], which is 1.
# The maximum element in the array is nums[1], which is 10.
# We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back.
# This results in 2 + 3 = 5 deletions, which is the minimum number possible.

# Example 2:
# Input: nums = [0,-4,19,1,8,-2,-3,5]
# Output: 3
# Explanation: 
# The minimum element in the array is nums[1], which is -4.
# The maximum element in the array is nums[2], which is 19.
# We can remove both the minimum and maximum by removing 3 elements from the front.
# This results in only 3 deletions, which is the minimum number possible.

# Example 3:
# Input: nums = [101]
# Output: 1
# Explanation:  
# There is only one element in the array, which makes it both the minimum and maximum element.
# We can remove it with 1 deletion.

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minIdx = 0
        maxIdx = 0
        
        N = len(nums)
        i=0
        while i<N:
            if nums[minIdx]>nums[i]:
                minIdx = i
            if nums[maxIdx]<nums[i]:
                maxIdx = i
                
            i+=1
            
        print(N, minIdx, maxIdx)
        
        first = min(minIdx, maxIdx)
        second = max(minIdx, maxIdx)
        
        if first==second:
            return first+1
        
        return min(second+1, N-first, first+1+N-second)
        
        # result = 0
        # if abs(minIdx-maxIdx)<N//2:
        #     if minIdx<=N//2 and maxIdx<=N//2:
        #         result = max(minIdx,maxIdx)+1
        #     else:
        #         result = (N - min(minIdx,maxIdx))
        # elif minIdx==maxIdx:
        #     result = minIdx+1
        # else:
        #     result = (min(minIdx,maxIdx)+1) + (N-max(minIdx,maxIdx))
        #return result