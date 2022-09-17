# 1248. Count Number of Nice Subarrays

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        ## To count odd/even using prefix sum technique, convert array elements to 1/0's
        i=0
        while i<len(nums):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
            i+=1
                
        #print(nums)
        result = 0
        prefixSum = {0:1}
        tempSum = 0
        for x in nums:
            tempSum+=x
            diff = tempSum-k
            
            result += prefixSum.get(diff,0)
            
            prefixSum[tempSum] = 1 + prefixSum.get(tempSum,0)           
        
        return result