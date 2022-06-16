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
        
        result = []
        def helper(node):
            if node:
                helper(node.left)
                result.append(node.val)
                helper(node.right)
        
        helper(root)
        
        return result
    
#         result = []
#         if not root:
#             return None
#         def helper(node):
#             # if not node:
#             #     return
            
#             nonlocal result
#             if node.left:
#                 result.append(helper(node.left))
            
#             if node:
#                 result.append(node.val)
            
#             if node.right:
#                 result.append(helper(node.right))
                
#         helper(root)
        
#         N=len(result)
#         i=0
#         j=0
#         while i<N:
#             if result[i]!=None:
#                 result[j]=result[i]
#                 j+=1
#             i+=1
#         result[j:]=[]
        
#         return result
                