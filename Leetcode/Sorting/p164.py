## 164. Maximum Gap

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        
        nums.sort()
        i=0
        maxGap = 0
        while i<len(nums)-1:
            maxGap = max(maxGap, nums[i+1]-nums[i])
            i+=1
            
        return maxGap