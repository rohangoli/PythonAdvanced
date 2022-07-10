## Construct Binary Tree from Inorder and Postorder Traversal

## https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/2242511/Python3-Solving-3-binary-tree-construction-problems-using-same-template

# Example 1:
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        midIdx = inorder.index(postorder[-1])
        
        root.left = self.buildTree(inorder[:midIdx], postorder[:midIdx])
        root.right = self.buildTree(inorder[midIdx+1:], postorder[midIdx:-1])
        
        return root