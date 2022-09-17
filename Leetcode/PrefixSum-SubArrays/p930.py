# 930. Binary Subarrays With Sum

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        result = 0
        
        ## TC - O(N), SC - O(N) for Hash Map
        preSumHM = defaultdict(lambda:0)
        preSumHM[0] = 1
        tempSum=0
        for x in nums:
            tempSum+=x
            if tempSum-goal in preSumHM:
                result+= preSumHM[tempSum-goal]
            
            preSumHM[tempSum]+=1
        
        ## TC - O(N^2) SC - O(N^2) >>> TLE
#         tempHM = {}
#         i=0
#         while i<len(nums):
#             j=i
#             while j<len(nums):
#                 if j==i:
#                     tempHM[(i,j)]=nums[j]
#                 else:
#                     tempHM[(i,j)]=nums[j]+tempHM[(i,j-1)]
                    
#                 if tempHM[(i,j)]==goal:
#                     result+=1
#                 j+=1
#             i+=1
            
            
        return result       