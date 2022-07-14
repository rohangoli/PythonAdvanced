## 496. Next Greater Element I

# Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

# Example 2:
# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tempS = []
        N = len(nums2)
        
        tempH = {}
        
        i=N-1
        while i>-1:
            #print(i, tempS, tempH)
            while tempS and tempS[-1]<nums2[i]:
                tempS.pop()
            
            if not tempS:
                tempH[nums2[i]]=-1
            else:
                tempH[nums2[i]]=tempS[-1]
                
            tempS.append(nums2[i])
            
            i-=1
         
        result = []
        for x in nums1:
            result.append(tempH[x])
        return result

    def nextGreaterElement_v2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        
        for x in nums1:
            ptr1 = nums2.index(x)
            ptr2 = ptr1+1
            result.append(-1)
            while ptr2<len(nums2):
                if nums2[ptr1]<nums2[ptr2]:
                    result[-1]=nums2[ptr2]
                    break
                ptr2+=1
                
        return result