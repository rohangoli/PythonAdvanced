## 897. Increasing Order Search Tree

# Example 1:
# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

# Example 2:
# Input: root = [5,1,7]
# Output: [1,null,5,null,7]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        self.result = []
        
        def helper(node):
            if not node:
                return
            
            helper(node.left)
            self.result.append(node.val)
            helper(node.right)
            
        helper(root)
        #print(self.result)
        
        root = TreeNode(self.result.pop(0))
        curr = root
        while self.result:
            curr.right = TreeNode(self.result.pop(0))
            curr = curr.right
            
        return root