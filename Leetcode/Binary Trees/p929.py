## Binary Tree Inorder Traversal

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
#         result = []
#         def helper(node):
#             if node:
#                 helper(node.left)
#                 result.append(node.val)
#                 helper(node.right)
        
#         helper(root)
        
#         return result
            
        curr = root
        tempS = []
        result = []
        
        while True:
            if curr:
                tempS.append(curr)
                curr = curr.left
            elif tempS:
                curr = tempS.pop()
                result.append(curr.val)
                curr = curr.right
            else:
                break
            
        return result
    
                