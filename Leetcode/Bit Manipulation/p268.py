## 268. Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tempHS = set()
        for x in nums:
            tempHS.add(x)
            
        for i in range(0,len(nums)+1):
            if i not in tempHS:
                return i