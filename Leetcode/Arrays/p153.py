## 153. Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def findPivot(start, end):
            while start<end:
                mid = start + (end-start)//2
                
                if start == mid:
                    if nums[start]<nums[start+1]:
                        return -1
                    return mid
                
                if nums[mid]>nums[end]:
                    start = mid
                else:
                    end = mid
                    
        idx = findPivot(0,len(nums)-1)
        #print(idx)
        if idx!=None:
            return nums[idx+1]
        else:
            return nums[0]
        