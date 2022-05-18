#  Largest Number At Least Twice of Others - O(N)

# Input: nums = [3,6,1,0]
# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.

# Input: nums = [1,2,3,4]
# Output: -1
# Explanation: 4 is less than twice the value of 3, so we return -1.

# Input: nums = [1]
# Output: 0
# Explanation: 1 is trivially at least twice the value as any other number because there are no other numbers.

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        N = len(nums)
        
        maxIdx = 0
        j=1
        while j<N:
            if nums[j]>nums[maxIdx]:
                maxIdx = j
            j+=1
        # print(maxIdx)
        
        j=0
        while j<N:
            if j==maxIdx:
                j+=1
                continue         
            if 2*nums[j]>nums[maxIdx]:
                return -1  
            j+=1
            
        return maxIdx
        