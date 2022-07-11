## Find Peak Element

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
#         ## O(N)
#         N = len(nums)
#         i=0
#         while i<N-1:
#             if nums[i]>nums[i+1]:
#                 return i
#             i+=1
            
#         return N-1
        
        ## First Implementation - Test Cases Not working
#         start = 0
#         end = len(nums)-1
#         mid = 0
#         while start<end:
#             mid = start + (end-start)//2
            
#             if start == mid:
#                 return mid+1
            
#             if nums[mid]>nums[mid+1]:
#                 end = mid
#             else:
#                 start = mid
                
#         return mid

        def helperSearch(nums, start, end):
            if start == end:
                return start
            
            mid = start + (end-start)//2
            if nums[mid]>nums[mid+1]:
                return helperSearch(nums, start, mid)
            else:
                return helperSearch(nums, mid+1, end)
            
        return helperSearch(nums, 0, len(nums)-1)