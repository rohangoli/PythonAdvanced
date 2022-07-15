## 404. Sum of Leaves

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

# Example 2:
# Input: root = [1]
# Output: 0

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        self.result = 0
        
        def helper(node):
            if not node:
                return 0
            
            if node.left and not node.left.left and not node.left.right:
                self.result+=node.left.val
                
            return helper(node.left) or helper(node.right)
        
        helper(root)
        
        return self.result