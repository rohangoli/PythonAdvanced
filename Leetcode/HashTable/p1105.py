## Intersection of Two Arrays

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=set()
        i=0

        # nums2 = set(nums2)
        M=len(nums1)
        while i<M:
            if nums1[i] in nums2:
                result.add(nums1[i])
            i+=1
            
        return result