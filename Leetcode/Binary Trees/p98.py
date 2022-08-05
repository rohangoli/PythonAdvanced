## Validate Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import numpy as np
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(Node, start, end):
            if not Node:
                return True
                
            if not start<Node.val<end:
                return False
            
            return helper(Node.left, start, Node.val) and helper(Node.right, Node.val, end)
        
        return helper(root, -np.inf, np.inf)
            
        
#         print(root)
#         if not root:
#             return True
        
#         if not root.right and not root.left:
#             return True
        
#         if not root.left and root.right:
#             return False
        
#         # if not root.right or not root.left:
#         #     return False
        
#         if root.left and not root.left.val<root.val:
#             print('LV Fail')
#             return False
        
#         if root.right and not root.val<root.right.val:
#             print('RV Fail')
#             return False
        
#         return self.isValidBST(root.left) and self.isValidBST(root.right)
        
        
#         if not root:
#             return True
        
#         if root.right and root.left:
#             if not root.left.val<root.val<root.right.val:
#                 return False
#             else:
#                 return self.isValidBST(root.left) and self.isValidBST(root.right)
#         return True