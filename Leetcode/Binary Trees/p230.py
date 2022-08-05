## 230. Kth Smallest Element in BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.elemL = []
        def helper(Node):
            if not Node:
                return
            
            helper(Node.left)
            self.elemL.append(Node.val)                
            helper(Node.right)
        
        helper(root)
        #print(self.elemL)
        
        return self.elemL[k-1]