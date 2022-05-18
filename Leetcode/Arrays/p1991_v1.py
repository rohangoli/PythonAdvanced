# Find the Middle Index in Array - O(N^2)

# Example 1:
# Input: nums = [2,3,-1,8,4]
# Output: 3
# Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
# The sum of the numbers after index 3 is: 4 = 4

# Example 2:
# Input: nums = [1,-1,4]
# Output: 2
# Explanation: The sum of the numbers before index 2 is: 1 + -1 = 0
# The sum of the numbers after index 2 is: 0

# Example 3:
# Input: nums = [2,5]
# Output: -1
# Explanation: There is no valid middleIndex.

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:           
        N = len(nums)
        
        j=0
        tot = 0
        while j<N:
            tot +=nums[j]
            j+=1
        
        pivot=0
        while pivot<N: 
            leftSum = 0
            # rightSum = 0

            j=0
            while j<pivot:
                leftSum += nums[j]
                j+=1
            
            rightSum = tot - leftSum - nums[pivot]
            # j=pivot+1
            # while j<N:
            #     rightSum +=nums[j]
            #     j+=1
                
            if leftSum==rightSum:
                return pivot
        
            pivot+=1          
            
        return -1