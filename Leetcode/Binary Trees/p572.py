## 572. Subtree of Another Tree

# Example 1:
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Example 2:
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val!=q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        self.result = False
        
        def helper(node, search):
            if not node:
                return False
            
            if node.val==search.val:
                temp = self.isSameTree(node, search)
                if temp:
                    self.result = True
            
            return helper(node.left, search) or helper(node.right, search)
        
        helper(root, subRoot)
        
        return self.result
        