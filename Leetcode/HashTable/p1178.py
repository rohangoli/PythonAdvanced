## Intersection of Two Arrays II

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp={}
        for num in nums1:
            if num not in temp:
                temp[num]=1
                continue
            temp[num]+=1
            
        result=[]
        for num in nums2:
            if num in temp and temp[num]>0:
                temp[num]-=1
                result.append(num)
        return result