## Move Zeroes

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        
        i=0
        j=0
        while i<N:
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
            i+=1
            
        while j<N:
            nums[j]=0
            j+=1
            
        return nums