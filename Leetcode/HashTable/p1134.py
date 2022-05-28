## 4Sum II

# Example 1:
# Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# Output: 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

# Example 2:
# Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# Output: 1

from collections import Counter
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        # map1 = {}
        # for c in nums3:
        #     for d in nums4:
        #         map1[c + d] = map1.get(c + d, 0) + 1
        # print(map1)   
        # count = 0
        # for a in nums1:
        #     for b in nums2:
        #         count += map1.get( -(a + b), 0)
        # return count
    
        result=0
        temp = Counter()
        for x in product(nums1,nums2):
            temp[sum(x)]+=1
        print(temp)  
        for x in product(nums3,nums4):
            var=-sum(x)
            if var in temp:
                result+=temp[var]
                
        return result