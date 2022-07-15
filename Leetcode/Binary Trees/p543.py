## 543. Diameter of Binary Tree

# Example 1:
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Example 2:
# Input: root = [1,2]
# Output: 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.result = 0
        
        def helper(node):
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            self.result = max(self.result, left+right)
            
            return 1 + max(left, right)
        
        helper(root)
        
        return self.result
    
#         if not root:
#             return 0
        
#         if not root.left and not root.right:
#             return 1
        
#         return self.diameterOfBinaryTree(root.left)+self.diameterOfBinaryTree(root.right)