## Single Number

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp={}
        for x in nums:
            if x not in temp:
                temp[x]=1
            else:
                temp[x]+=1
                
        for x,y in temp.items():
            if y==1:
                return x
        
#         N=len(nums)
        
#         temp=[0]*(abs(max(nums))+1)
#         i=0
#         while i<N:
#             temp[nums[i]]+=1
#             i+=1
            
#         i=1
#         while i<len(temp):
#             if temp[i]==1:
#                 break
#             i+=1
        
#         return i