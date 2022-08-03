## 128. Longest Consecutive Sequence

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        numSet = set(nums)
        
        result = 0
        for x in nums:
            if x-1 not in numSet:
                length=1
                while x+length in numSet:
                    length+=1
                
                result = max(result,length)
        
        return result