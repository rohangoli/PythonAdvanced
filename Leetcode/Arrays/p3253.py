## Merge Sorted Array

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """       
        
        M=m
        N=n            
       
        if n==0:
            return True
        
        i=M+N-1
        j=M-1
        k=N-1
        while j>-1 and k>-1:
            # print(i,j,k,nums1,nums2)
            
            if nums1[j]>=nums2[k]:
                nums1[i]=nums1[j]
                j-=1
            else:
                nums1[i]=nums2[k]
                k-=1
            
            # if k>-1 and nums1[j]<=nums2[k]:
            #     nums1[i]=nums2[k]
            #     k-=1
            # elif j>-1 and nums1[j]>=nums2[k]:
            #     nums1[i]=nums1[j]
            #     j-=1

            # print(i,j,k,nums1,nums2)
            # print('-'*15)
            i-=1
          
        if k>=0:
            nums1[:k+1]=nums2[:k+1]
        # while k>=0:
        #     nums1[i]=nums2[k]
        #     k-=1
            
        # print(nums1)
        # print('-'*15)