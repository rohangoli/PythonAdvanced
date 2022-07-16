## 35. Search Insert Position

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        i=0
        while i<N and nums[i]<=target:
            if nums[i]==target:
                break
            
            i+=1
            
        return i