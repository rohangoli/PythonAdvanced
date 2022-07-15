## 1022. Sum of Root to Binary Numbers

# Example 1:
# Input: root = [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

# Example 2:
# Input: root = [0]
# Output: 0

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        self.result = 0
        
        def str2dec(num):
            c = 0
            i=len(num)-1
            e = 0
            while i>-1:
                c+= int(num[i])*(2**e)
                i-=1
                e+=1
            return c
        
        def helper(node,path):
            if not node:
                return
            
            path+=str(node.val)
            if not node.left and not node.right:
                self.result+=str2dec(path)
            
            return helper(node.left, path) or helper(node.right, path)
        
        helper(root, '')
        return self.result 