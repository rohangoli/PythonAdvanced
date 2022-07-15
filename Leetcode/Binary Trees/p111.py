## 111. Minimum Depth of Binary Tree

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Example 2:
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.result = 999999
        
        if not root:
            return 0
        
#         def helper(node):
#             if not node:
#                 return 0
            
#             left = helper(node.left)
#             right = helper(node.right)
            
#             print(node.val, left, right)
            
#             return 1+max(left,right)

        def helper2(node, depth):
            #print(node, depth)
            if not node:
                return 1
            
            if not node.left and not node.right:
                self.result = min(self.result, depth)
                
            return max(helper2(node.left,depth+1),helper2(node.right, depth+1))
        
        helper2(root,1)
            
        return self.result