## Construct Binary Tree from Preorder and Inorder Traversal

# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        midIdx = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:midIdx+1], inorder[:midIdx])
        root.right = self.buildTree(preorder[midIdx+1:], inorder[midIdx+1:])
        
        return root