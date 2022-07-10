## Search in Rotated Sorted Array

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def findPivot(nums, start, end):
            while start<end:
                mid = start + (end-start)//2

                if start==mid:
                    if nums[start]<nums[start+1]:
                        return -1
                    return mid

                if nums[mid]>nums[end]:
                    start = mid
                else:
                    end = mid
        
        def binarySearch(nums, start, end, target):
            while start<=end:
                mid = start + (end-start)//2
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
            return -1
        
        start = 0
        end = len(nums)-1
        pivot = findPivot(nums, start, end)
        
        print(pivot)
        
        if pivot == -1 or pivot ==None:
            return binarySearch(nums, start, end, target)
        
        if nums[pivot+1]<=target<=nums[end]:
            return binarySearch(nums, pivot+1, end, target)
        else:
            return binarySearch(nums, start, pivot, target)
            
        # left = 0
        # right = len(nums)-1
        # while left<=right:
        #     mid = left + (right-left)//2
        #     print(left, mid, right)
        #     if target==nums[mid]:
        #         print('-'*5, mid)
        #         return mid
        #     elif target<nums[left] and target<nums[mid]:
        #     #elif target<=nums[right]<nums[left]:
        #         left = mid+1
        #     elif target>=nums[left] and target<nums[mid]:
        #         right = mid-1
        #     elif target>nums[mid] and target>nums[right]:
        #         right = mid -1
        #     else:
        #         right = mid-1
        # print('-'*5, -1)        
        # return -1