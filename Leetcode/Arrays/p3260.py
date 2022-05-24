## Sort Array By Parity

# Example 1:
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Example 2:
# Input: nums = [0]
# Output: [0]

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        N=len(nums)
        
        i=0
        j=N-1
        
        while i<j:
            if nums[i]%2!=0 and nums[j]%2==0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
            elif nums[i]%2!=0 and nums[j]%2!=0:
                j-=1
            else:
                i+=1
        
            # print(nums)
        
        return nums            