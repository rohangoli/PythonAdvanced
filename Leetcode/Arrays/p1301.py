## Max Consecutive Ones

# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result=0
        
        N=len(nums)
        i=0
        temp=0
        while i<N:
            if nums[i]==1:
                temp+=1
            else:
                result=max(result,temp)
                temp=0
            i+=1
            
        result = max(result,temp)
            
        return result