## Squares of a Sorted Array

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N=len(nums)
        i=0
        while i<N:
            nums[i]=nums[i]**2
            i+=1
            
        nums.sort()
        
        return nums