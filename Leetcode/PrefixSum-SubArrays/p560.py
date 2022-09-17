## 560. Subarray Sum Equals K

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0:1}
        result = 0
        
        tempSum = 0
        for x in nums:
            tempSum+=x
            diff = tempSum-k
            
            result+= prefixSums.get(diff,0)
            
            prefixSums[tempSum] = 1 + prefixSums.get(tempSum,0)
        
        return result