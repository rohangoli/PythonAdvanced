## 228. Summary Ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return
        result=[]
        i=1
        curr = 0
        lowR = nums[curr]
        highR = nums[curr]
        while i<len(nums):
            if nums[i]==nums[i-1]+1:
                highR = nums[i]
            else:
                if lowR==highR:
                    result.append(str(lowR))
                else:
                    result.append("{}->{}".format(lowR,highR))
                curr = i
                lowR = highR = nums[curr]
            i+=1
        if lowR==highR:
            result.append(str(lowR))
        else:
            result.append("{}->{}".format(lowR,highR))
            
        return result