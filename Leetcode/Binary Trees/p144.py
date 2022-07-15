## 144. Binary Tree Preorder Traversal

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,2,3]

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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        tempS = [root]
        while tempS:
            curr = tempS.pop()
            if curr:
                result.append(curr.val)
                tempS.append(curr.right)
                tempS.append(curr.left)
        return result
        
#         result = []
#         def helper(node):
#             if node:
#                 result.append(node.val)
#                 if node.left:
#                     helper(node.left)
#                 if node.right:
#                     helper(node.right)
                
#         helper(root)
#         return result