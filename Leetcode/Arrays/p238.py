## 238. Product of Array Except Self

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result = [1]*N
        left_mult = 1
        right_mult = 1
        
        i=1
        while i<N:
            #print(i, left_mult, result)
            left_mult *= nums[i-1]
            result[i] = left_mult
            i+=1
            
        j=N-2
        while j>-1:
            #print(j, right_mult, result)
            right_mult *= nums[j+1]
            result[j] *= right_mult
            j-=1
            
        return result