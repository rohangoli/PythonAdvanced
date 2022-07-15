## 108. Convert Sorted Array to Binary Search Tree

# Example 1:
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        def helper(arr):
            if len(arr)==0:
                return
            
            idx = len(arr)//2
            #print(idx, arr[idx], arr[:idx], arr[idx+1:])
            node = TreeNode(arr[idx])
            node.left = helper(arr[:idx])
            node.right = helper(arr[idx+1:])
            
            return node
            
        return helper(nums)
        
                
    