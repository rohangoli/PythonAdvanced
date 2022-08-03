## 15. 3Sum

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # numSet = set(nums)
        N = len(nums)
        result=[]
        # i=0
        # while i<N-1:
        #     j=i+1
        #     while j<N:
        #         if -(nums[i]+nums[j]) in numSet:
        #             result.append([nums[i], nums[j], -(nums[i]+nums[j])])
        #             numSet.remove(-(nums[i]+nums[j]))
        #         j+=1
        #     i+=1
        
        # i=0
        # while i<N-2:
        #     j=i+1
        #     while j<N-1:
        #         k=j+1
        #         while k<N:
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 result.append([nums[i], nums[j], nums[k]])
        #             k+=1
        #         j+=1
        #     i+=1
        
        nums.sort()
        for idx, val in enumerate(nums):
            if idx>0 and val==nums[idx-1]:
                continue
            
            l=idx+1
            r=N-1
            while l<r:
                threeSum = val + nums[l] + nums[r]
                if threeSum<0:
                    l+=1
                elif threeSum>0:
                    r-=1
                else:
                    result.append([val,nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l-1]==nums[l]:
                        l+=1
                        
        return result
            
        
        #return result