## 1909. Remove One Element to Make the Array Strcitly Increasing

from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def checkIncSeq(array):
            i=0
            while i<len(array)-1:
                if array[i+1]<=array[i]:
                    return False
                i+=1
            return True

        j=0
        while j<len(nums):
            if checkIncSeq(nums[:j]+nums[j+1:]):
                return True
            j+=1

        return False