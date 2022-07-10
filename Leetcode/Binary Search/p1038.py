## Binary Search

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return
        
        N = len(nums)
        
#         def helper(start, end, target):
#             midIdx = start+(end-start)//2
#             #print("Start: {} End: {}".format(start,end))
#             #print("Curr.Idx: {} Value: {} Target:{}".format(midIdx, nums[midIdx], target))
#             if target == nums[midIdx]:
#                 return midIdx
#             elif target > nums[midIdx] and end-midIdx>0:
#                 return helper(midIdx+1, end, target)
#             elif target < nums[midIdx] and midIdx-start>0:
#                 return helper(start,midIdx-1, target)
            
#             return -1
            
#         #print('-'*10)    
#         return helper(0,N-1,target)
        
        left = 0
        right = N-1
        while left<=right:
            mid = left + (right-left)//2
            #print(left, mid, right)
            if target == nums[mid]:
                #print('-'*5)
                return mid
            elif target>nums[mid]:
                left = mid+1
            else:
                right = mid-1
        #print('-'*5)
        return -1