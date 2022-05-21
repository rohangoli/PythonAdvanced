## Minimum Size Subarray Sum

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # nums.sort()
        N = len(nums)
        
        if nums==None or N<=1:
            return 0
                
        i=0
        j=0
        
        result = N
        tempSum=0
        exists = False
        while i<=N:
            if tempSum>=target:
                exists = True
                if j==i-1:
                    return 1
                
                result = min(result,i-j)
                tempSum -= nums[j]
                j+=1
                
            else:
                if i==N:
                    break
                tempSum+=nums[i]
                i+=1
                
        if exists:
            return result
        else:
            return 0
        
#         result=N+1
#         tempSum=0
        
#         while i<N:
#             if tempSum>=target:
#                 print(result,i,j, i-j)
#                 result = min(result, i-j)
#                 tempSum -= nums[j]
#                 j+=1
#             else:
#                 tempSum += nums[i]
#                 i+=1
#             print(tempSum,i)
                
#         if result>N+1:
#             return 0
#         else:
#             return result