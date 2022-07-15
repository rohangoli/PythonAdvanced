## 110. Balanced Binary Tree

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #print('-'*20)
        self.result = 0
        def helper(node):
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            #print(node.val, node.left,'->', left, node.right,'->', right)
            if abs(left-right)>1:
                self.result = -1
            
            return 1+max(left,right)
        
        helper(root)
        #print(self.result)
        if self.result==-1:
            return False
        else:
            return True
        
        
#         if not root:
#             return True
        
#         if not root.left and root.right:
#             return False
#         else:
#             return self.isBalanced(root.left) and self.isBalanced(root.right)